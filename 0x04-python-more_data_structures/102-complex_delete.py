#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dictionary_copy = a_dictionary.copy()
    for key, item in a_dictionary_copy.items():
        if item == value:
            del a_dictionary[key]
            continue
    return a_dictionary
