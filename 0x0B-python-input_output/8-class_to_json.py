#!/usr/bin/python3
"""
module
"""


def class_to_json(obj):
    """Returns the dictionary description with simple
    data structure (list, dict, str, int and bool) for JSON
    serialization

    Args:
        obj (object): Object to serialize

    Returns:
        dict: The dictionary description
    """
    return obj.__dict__