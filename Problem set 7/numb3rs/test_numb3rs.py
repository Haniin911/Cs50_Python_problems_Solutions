import pytest
from numb3rs import validate


def test_valid_addresses():
    assert validate("0.0.0.0") is True
    assert validate("255.255.255.255") is True


def test_invalid_addresses_and_types():
    assert validate("1.2.3") is False
    assert validate("1.2.3.4.5") is False
    assert validate("256.100.100.100") is False
    assert validate("000.001.010.100") is False
