#!/usr/bin/python3
"""
Module
"""


def is_same_class(obj, a_class):

    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: An object to check.
        a_class: The specified class.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) == a_class
