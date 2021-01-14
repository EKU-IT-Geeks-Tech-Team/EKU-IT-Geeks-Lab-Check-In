import re
import time
from datetime import datetime
from openpyxl import load_workbook


# returns either a swipenumber as a string or None
def parse_card(raw_card_input: str):
    '''
    https://docs.python.org/3/library/re.html#match-objects
    re.search() searches the entire string for the pattern
        returns a Match() object
    Match.group(0) returns the entire match as a single string
    '''
    match = re.search(
        r"(?<=;1234567)\d{9}(?=\=123456789012345\?)", raw_card_input)
    if match:
        return match.group(0)


# i found this on stack overflow and forgot to copy the link oops
def utc2local(utc: datetime):
    epoch = time.mktime(utc.timetuple())
    offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
    return utc + offset

def open_excel(filename):
    workbook = load_workbook(filename = filename)
    worksheet = workbook.active

    for row in worksheet.iter_rows(min_row=2):
        for cell in row:
            print(cell.value)
