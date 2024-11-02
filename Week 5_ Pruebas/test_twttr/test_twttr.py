import pytest
from twttr import shorten

# DEFAUL TEST
def test_default():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hello") == "Hll"
    assert shorten("What's your name?") == "Wht's yr nm?"

# LOWERCASE VOWELS TEST
def test_lower():
    assert shorten("Hello, World") == "Hll, Wrld"

# LOWERCASE VOWELS TEST
def test_capitalice():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"

# LOWERCASE VOWELS TEST
def test_number():
    assert shorten("CS50") == "CS50"

# ERROR CASE TEST
def test_error():
    with pytest.raises(TypeError):
        shorten(1)
