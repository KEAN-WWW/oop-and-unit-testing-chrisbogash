"""This is the addition test file"""
from app.addition import add


def test_addition():
    """ Add the numbers"""
    assert add(2, 2) == 4
