#!/usr/bin/python3
"""
A module for addition
"""


def add_integer(a, b=98):
    """
    returns the addition of two numbers

    Parameters:
    a (int or float): first number
    b (int or float): second number. Defaults to 98

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
