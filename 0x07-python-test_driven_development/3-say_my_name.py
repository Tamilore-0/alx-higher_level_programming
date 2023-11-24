#!/usr/bin/python3
"""
A module for names
"""


def say_my_name(first_name, last_name=""):
    """
    Print a formatted string with the provided first and last names.

    Args:
        first_name (str): The first name to be included in the output.
        last_name (str, optional): The last name to be included in the output.
        Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
