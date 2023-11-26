#!/usr/bin/python3
"""
This module provides a function 'add_integer' for performing addition.
The function takes two parameters:
    'a' and 'b', then returns their sum.
"""


def add_integer(a, b=98):
    """
    returns the addition of two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
