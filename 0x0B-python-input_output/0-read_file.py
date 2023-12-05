#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
    print(content)
