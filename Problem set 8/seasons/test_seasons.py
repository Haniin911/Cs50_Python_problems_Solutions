# test_seasons.py
from datetime import date
import pytest
from seasons import get_birthdate, minutes_since, number_to_words

def test_minutes_since():
    assert minutes_since(date.today()) == 0
    assert minutes_since(date.today().replace(day=1, month=1, year=2000)) > 0

def test_number_to_words():
    assert number_to_words(0) == "Zero"
    assert number_to_words(525600) == "Five hundred twenty five thousand six hundred"
    assert "million" in number_to_words(1000000).lower()

def test_invalid_date_format(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "invalid-date")
    import sys
    with pytest.raises(SystemExit):
        get_birthdate()
