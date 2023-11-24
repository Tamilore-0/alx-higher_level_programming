#!/usr/bin/python3
"""
Text indentation module
"""


def text_indentation(text):
    """
    Prints sentences from the given text on separate lines.

    Args:
    text (str): The input text.

    Raises:
    TypeError: If the input is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    string = []
    for i in range(len(text)):
        if text[i] not in ['.', '?', ':']:
            string.append(text[i])
            continue
        else:
            string.append(text[i])
            string.append("\n")
            new_string = "".join(string)
            new_string = new_string.lstrip(" ").rstrip(" ")
            print(new_string)
            string = []

    if string:
        new_string = "".join(string)
        new_string = new_string.lstrip(" ").rstrip(" ")
        print(new_string, end="")
