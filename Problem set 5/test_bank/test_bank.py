from bank import value

def test_hello():
    assert value("Hello") == "$0"

def test_hey():
    assert value("Hey") == "$20"

def test_other():
    assert value("Good morning") == "$100"
