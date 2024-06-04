from lib.report_length import *


def test_report_given_length():
    the_string = report_length("Hello World!")
    length = 12
    assert length == 12