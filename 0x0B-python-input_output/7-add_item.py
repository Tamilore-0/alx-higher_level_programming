#!/usr/bin/python3
"""
7-add_item:
"""


import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    
    filename = "add_item.json"

    try:
        arg_list = load(filename)
    except:
        arg_list = []

    for arg in sys.argv[1:]:
        arg_list.append(arg)
    save(arg_list, filename)
