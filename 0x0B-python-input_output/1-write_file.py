#!/usr/bin/python3
"""
    1-write_file: write_file()
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters
    """
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
    return num
