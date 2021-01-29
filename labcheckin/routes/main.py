from flask import Blueprint, flash, request, redirect, url_for, render_template
from flask import json
from labcheckin.models import Seat, Student, Transaction
from labcheckin import db
from labcheckin.utilities import parse_card, utc2local
from datetime import datetime
from labcheckin.models import Seat


main = Blueprint(
    "main",
    __name__
)


@main.route("/")
def index():
    current_student_ids = db.session.query(
        Transaction.student_id
    ).filter_by(out_time=None)

    # get students currently in lab from list of student_ids
    current_students = Student.query.filter(
        Student.student_id.in_(current_student_ids)).all()

    current_swipe_numbers = [s.swipe_number for s in current_students]

    seats = Seat.query.all()
    seat_statuses = {}

    seat_types = set([seat.type for seat in seats])

    for seat_type in seat_types:
        for seat in seats:
            if seat.type == seat_type:
                seat_statuses.setdefault(seat_type, [])
                seat_statuses[seat_type].append(seat)

    '''

    seat_statuses['Booth'] = [B1, B2, B3]
    seat_statuses['WIN'] = [WIN1, WIN2]

    '''

    return render_template(
        "main/index.html.j2",
        current_students=current_students,
        current_swipe_numbers=current_swipe_numbers,
        get_student_seat=get_student_seat,
        seat_statuses=seat_statuses,
    )


@main.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "GET":
        return render_template("main/add_student.html.j2")
    else:
        name = request.form.get("fullName")
        studentID = request.form.get("studentID")
        raw_swipe_input = request.form.get("swipeNum")
        email = request.form.get("email")

        swipeNum = parse_card(raw_swipe_input)

        new_student = Student(
            student_id=studentID,
            full_name=name,
            swipe_number=swipeNum,
            email=email
        )

        db.session.add(new_student)
        db.session.commit()

        flash("Student added successfully", "success")

        return redirect(url_for("main.index"))


@main.route("/validate_card/<card_input>", methods=["GET"])
def validate_card(card_input):
    print(card_input)
    swipe_number = parse_card(card_input + "?")
    seatTypes = get_available_seat_types()
    print(seatTypes)
    if swipe_number:
        return json.dumps({
            "swipe_number": swipe_number,
            "seatTypes": seatTypes
        })
    return json.dumps({})


@main.route("/create_transaction", methods=["POST"])
def create_transaction():
    swipe_number = request.form.get("swipe_number")
    student = Student.query.filter_by(
        swipe_number=swipe_number).first()

    if student:
        last_t = Transaction.query.filter_by(
            student=student).order_by(Transaction.in_time.desc()).first()

        # if the transaction and the out_time does not exist update it with time out
        if last_t and not last_t.out_time:
            seat = last_t.seat
            seat.status = "Needs Cleaning"

            currentTime = datetime.now()
            last_t.out_time = currentTime
            db.session.commit()

        # otherwise create a new transaction
        else:
            seatType = request.form.get("options")
            if seatType:
                seat = get_next_available(seatType)

                flash(f"{seat.label} has been assigned", "success")

                seat.status = "In Use"

                t = Transaction(student_id=student.student_id, seat_id=seat.id)
                db.session.add(t)
                db.session.commit()
            else:
                flash("You must select a seat type", "danger")
    else:
        flash("No student found", "danger")

    return redirect(url_for("main.index"))


@main.route("/end_transaction/<seat_label>", methods=["GET"])
def end_transaction(seat_label: str):
    seat = Seat.query.filter_by(label=seat_label).first()
    last_t = Transaction.query.filter_by(seat=seat).order_by(
        Transaction.in_time.desc()).first()

    seat.status = "Needs Cleaning"
    currentTime = datetime.now()
    last_t.out_time = currentTime

    db.session.commit()
    return redirect(url_for("main.index"))


@main.route("/seat_cleaned/<seat_label>", methods=["GET"])
def seat_cleaned(seat_label: str):
    seat = Seat.query.filter_by(label=seat_label).first()
    seat.status = "Open"
    db.session.commit()
    return redirect(url_for("main.index"))


def get_available_seat_types():
    # create empty list to store available seat types
    seatTypes = []

    availableSeats = Seat.query.filter_by(status="Open").all()

    for seat in availableSeats:
        seatTypes.append(seat.type)

    # shrinks the list to only unique values. ["WIN", "WIN", "MAC"] -> ["WIN", "MAC"]
    seatTypes = list(set(seatTypes))

    return seatTypes


def get_student_seat(student):
    last_t = Transaction.query.filter_by(student=student).order_by(
        Transaction.in_time.desc()).first()
    seat = last_t.seat
    return seat


def get_next_available(seat_type: str) -> Seat:
    seat_type = seat_type.upper()

    priorities = {
        "PC": (
            "WIN1", "WIN12", "WIN9", "WIN7", "WIN5", "WIN11", "WIN2", "WIN8", "WIN4", "WIN6"
        ),
        "MAC": (
            "MAC14", "MAC10", "MAC13"
        ),
        "BOOTH": (
            "B1", "B5", "B3", "B2", "B4"
        ),
        "SCANNER": (
            "SCN3",
        )
    }

    for seat_label in priorities[seat_type]:
        seat = Seat.query.filter_by(label=seat_label).first()

        if seat.status == "Open":
            return seat
    return None
