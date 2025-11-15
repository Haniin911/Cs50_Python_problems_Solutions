from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed():
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert shorten("1234") == "1234"

def test_symbols():
    assert shorten("CS50!") == "CS50!"
