import pytest
from fuel import convert, gauge


# ---- Tests for convert() ----

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_value_error():
    # b > a (invalid)
    with pytest.raises(ValueError):
        convert("2/1")

    # decimal values
    with pytest.raises(ValueError):
        convert("1.5/2")

    # missing slash
    with pytest.raises(ValueError):
        convert("12")

    # negative numbers
    with pytest.raises(ValueError):
        convert("-1/2")

    # random string
    with pytest.raises(ValueError):
        convert("hello/world")


# ---- Tests for gauge() ----

def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
