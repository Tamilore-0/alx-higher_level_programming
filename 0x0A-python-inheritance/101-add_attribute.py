#!/usr/bin/python3
"""
...
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception if the object can't have a new attribute.

    Args:
        obj: The object to which the new attribute will be added.
        name (str): The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
