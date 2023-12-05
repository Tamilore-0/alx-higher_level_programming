#!/usr/bin/python3
"""
7-add_item:
"""


import sys
import os
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.txt"

    if not os.path.exists(filename):
        mode = 'w'
    else:
        mode = 'a'        
                                  
    with open(filename, mode) as file:
        for arg in sys.argv[1:]:
            file.write(f"{arg}\n")

    with open(filename, 'r') as file1:
        lists = file1.read().splitlines()

    save(lists, "add_item.json")