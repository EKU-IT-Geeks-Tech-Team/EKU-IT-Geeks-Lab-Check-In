from labcheckin import create_app
import os

app = create_app()

'''
WSGI stands for: Web Server Gateway Interface
"It is a specification that describes how a web server communicates with web applications,
    and how web applications can be chained together to process one request."

"WSGI[1] is not a server, a python module, a framework, an API or any kind of software. It is just an interface specification by which server and application communicate."
"A WSGI server (meaning WSGI compliant) only receives the request from the client,
    pass it to the application and then send the response returned by the application to the client.
    It does nothing else. All the gory details must be supplied by the application or middleware."

All this to say, this is the recommended way to create a flask server.
'''

# create sqlite db file if not exists
if app.config["ENV"] == "development" and not os.path.exists(os.path.join(app.root_path, app.config["DB_FILENAME"])):
    with app.app_context():
        from labcheckin import db
        from labcheckin.models import *
        db.create_all()

        print(
            f"Created database file at: {os.path.join(app.root_path, app.config['DB_FILENAME'])}"
        )

        # for now, this is the only data that will be in the local db
        test_student = Student(
            student_id="901000000",
            full_name="Test Student",
            swipe_number="901000000"
        )

        B1 = Seat(
            type="Booth",
            label="B1",
            status="Open"
        )

        B2 = Seat(
            type="Booth",
            label="B2",
            status="Open"
        )

        B3 = Seat(
            type="Booth",
            label="B3",
            status="Open"
        )

        B4 = Seat(
            type="Booth",
            label="B4",
            status="Open"
        )

        B5 = Seat(
            type="Booth",
            label="B5",
            status="Open"
        )

        WIN1 = Seat(
            type="PC",
            label="WIN1",
            status="Open"
        )

        WIN2 = Seat(
            type="PC",
            label="WIN2",
            status="Open"
        )

        WIN4 = Seat(
            type="PC",
            label="WIN4",
            status="Open"
        )

        WIN5 = Seat(
            type="PC",
            label="WIN5",
            status="Open"
        )

        WIN6 = Seat(
            type="PC",
            label="WIN6",
            status="Open"
        )

        WIN7 = Seat(
            type="PC",
            label="WIN7",
            status="Open"
        )

        WIN8 = Seat(
            type="PC",
            label="WIN8",
            status="Open"
        )

        WIN9 = Seat(
            type="PC",
            label="WIN9",
            status="Open"
        )

        WIN11 = Seat(
            type="PC",
            label="WIN11",
            status="Open"
        )

        WIN12 = Seat(
            type="PC",
            label="WIN12",
            status="Open"
        )

        SCN3 = Seat(
            type="Scanner",
            label="SCN3",
            status="Open"
        )

        MAC10 = Seat(
            type="Mac",
            label="MAC10",
            status="Open"
        )

        MAC13 = Seat(
            type="Mac",
            label="MAC13",
            status="Open"
        )

        MAC14 = Seat(
            type="Mac",
            label="MAC14",
            status="Open"
        )

        db.session.add(jadon)
        db.session.add(B1)
        db.session.add(B2)
        db.session.add(B3)
        db.session.add(B4)
        db.session.add(B5)
        db.session.add(WIN1)
        db.session.add(WIN2)
        db.session.add(WIN4)
        db.session.add(WIN5)
        db.session.add(WIN6)
        db.session.add(WIN7)
        db.session.add(WIN8)
        db.session.add(WIN9)
        db.session.add(WIN11)
        db.session.add(WIN12)
        db.session.add(SCN3)
        db.session.add(MAC10)
        db.session.add(MAC13)
        db.session.add(MAC14)
        db.session.commit()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
