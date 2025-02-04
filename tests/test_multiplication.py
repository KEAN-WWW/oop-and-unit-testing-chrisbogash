"""This is the multiplication test file"""
from app.multiplication import multiply


def test_multiplication():
    """ Multiply the numbers"""
    assert multiply(2, 2) == 4
