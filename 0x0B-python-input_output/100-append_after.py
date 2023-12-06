#!/usr/bin/python3
"""
Contains the "append after" function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends "new_string" after a line containing
    "search_string" in "filename" """
    lines_to_write = []

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line == "":
                break
            lines_to_write.append(line)
            if search_string in line:
                lines_to_write.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines_to_write)
