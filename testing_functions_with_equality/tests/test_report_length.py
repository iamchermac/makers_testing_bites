from lib.report_length import *

def test_report_length_hello_returns_5():
    result = report_length("hello")
    assert result == "This string was 5 characters long."
    