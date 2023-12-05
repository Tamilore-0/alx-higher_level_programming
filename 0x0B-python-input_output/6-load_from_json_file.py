#!/usr/bin/python3
"""
6-load_from_json_file: load_from_json
"""


import json


def load_from_json_file(filename):
    """
        loads an object to from JSON file.
        Args:
            filename (str): name of file.
    """
    with open(filename, 'r') as j_file:
        obj = json.load(j_file)
    return obj
