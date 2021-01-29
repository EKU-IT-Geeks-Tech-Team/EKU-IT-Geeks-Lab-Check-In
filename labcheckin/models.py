from labcheckin import db
from datetime import datetime
from sqlalchemy.orm import relationship


class Student(db.Model):
    student_id = db.Column(db.String(9), primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    swipe_number = db.Column(db.String(9), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    transactions = relationship("Transaction", back_populates="student")

    def __repr__(self):
        return '<User %r>' % self.student_id

# the database logging each transaction we make


class Transaction(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    student_id = db.Column(
        db.String(9),
        db.ForeignKey(
            "student.student_id"),
        nullable=False
    )
    student = relationship("Student", back_populates="transactions")

    # we are not doing the directional transactions anymore
    # now we logg in time and out time in one transaction
    in_time = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    out_time = db.Column(
        db.DateTime,
        nullable=True
    )

    seat_id = db.Column(
        db.String(2),
        db.ForeignKey("seat.id"),
        nullable=False
    )

    seat = relationship("Seat", back_populates="transactions")

    def __repr__(self):
        return f"{self.student_id} {self.time} {'IN' if self.direction else 'OUT'}"

    def __str__(self):
        return f"{self.student_id} {self.time} {'IN' if self.direction else 'OUT'}"

# the database logging each of the seats in the lab


class Seat(db.Model):
    # Generic Primary Key
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    # Type of seat. for example booth, or pc, or mac, or scanner
    type = db.Column(
        db.String(10),
        nullable=False
    )

    # full label for a seat. Ie Pc1, Booth1, Scanner1, Mac3, etc.
    label = db.Column(
        db.String(15),
        nullable=False,
        unique=True
    )
    # Value for if someone is currently in seat or it needs cleaned
    status = db.Column(
        db.String(30),
        nullable=False,
        default="Open"
    )
    transactions = relationship("Transaction", back_populates="seat")
