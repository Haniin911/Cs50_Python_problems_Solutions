from plates import is_valid

def test_valid_simple():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_starts_with_letters():
    assert is_valid("50CS") == False
    assert is_valid("C5S0") == False

def test_zero_rule():
    assert is_valid("CS05") == False   # first number cannot be 0

def test_numbers_after_letters_only():
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False

def test_symbols():
    assert is_valid("HELLO, WORLD") == False
