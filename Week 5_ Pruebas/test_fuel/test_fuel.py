import pytest
from fuel import convert
from fuel import gauge

# TEST CONVERT, RETURN INT
def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100

# TEST CONVERT ABOVE 100
def test_above_100():
    with pytest.raises(ValueError):
        convert("4/1")
        convert("uno/cuatro")

# TEST CONVERT, ZERO DIVISION
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# TEST GAUGE
def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"

def test_error():
    with pytest.raises(AttributeError):
        convert(1)
