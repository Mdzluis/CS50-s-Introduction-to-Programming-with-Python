import pytest
from plates import is_valid

# BEGINNING TEST ALPHABETIC
def test_alphabetic():
    assert is_valid("50") == False

# LENGTH TEST
def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS2024") == True
    assert is_valid("CS") == True

# BEGINNING TEST WITH LETTERS
def test_beginning_alphabetical():
    assert is_valid("50cs") == False

# BEGINNING TEST WITH ZERO
def test_zero():
    assert is_valid("CS05") == False

# TEST OF NUMBERS IN PLATE
def test_position_number():
    assert is_valid("CS500P") == False
    assert is_valid("CSP500") == True

# TEST PI
def test_number():
    assert is_valid("PI3.14") == False

def test_error():
    with pytest.raises(TypeError):
        is_valid(1)
