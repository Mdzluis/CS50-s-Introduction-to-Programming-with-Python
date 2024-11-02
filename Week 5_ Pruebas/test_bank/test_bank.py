import pytest
from bank import value

# GREETING TEST WITH CAPITAL HELLO
def test_hello_capitalice():
    assert value("Hello") ==  0
    assert value("HELLO") ==  0

# GREETING TEST WITH HELLO LOWERCASE
def test_hello_lower():
    assert value("hello") ==  0

# GREETING TEST WITH H
def test_greeting_with_h():
    assert value("Hey") ==  20
    assert value("How you doing?") ==  20

# GREETING TEST WITHOUT H
def test_greeting_without_h():
    assert value("What's happening") ==  100

# GREETING TEST WITH NUMBER
def test_number():
    assert value("CS50") == 100

# ERROR CASE TEST
def test_error():
    with pytest.raises(AttributeError):
        value(1)
