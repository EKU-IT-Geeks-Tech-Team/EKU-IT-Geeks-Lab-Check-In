from labcheckin.utilities import import_students_from_csv
import sys
from labcheckin import create_app

app = create_app()

with app.app_context():
    filename = sys.argv[1]
    import_students_from_csv(filename)
