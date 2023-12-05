#!/usr/bin/python3
"""
7-add_item:
"""


import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    # Load an existing list or create an empty list
    items_list = load('add_item.json') or []

    # Add command line arguments to the list
    items_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save(items_list, 'add_item.json')
