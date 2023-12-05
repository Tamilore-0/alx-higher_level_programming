#!/usr/bin/python3
"""
    2-append_write: append_write()
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8)
    and return the number of characters added.

    :param filename: The name of the file.
    :param text: The string to append to the file.
    :return: The number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        num_characters_added = f.write(text)
    return num_characters_added
