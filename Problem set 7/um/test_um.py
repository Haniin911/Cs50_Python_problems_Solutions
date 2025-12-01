import pytest
from um import count

def test_basic():
    assert count("um") == 1

def test_multiple_occurrences():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3

def test_ignore_substrings():
    assert count("yummy") == 0
    assert count("summary") == 0

def test_mixed_text():
    assert count("Hello, um, world!") == 1
