#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary_copy = a_dictionary.copy()
    for key, value in a_dictionary_copy.items():
        a_dictionary_copy[key] = value * 2
    return a_dictionary_copy
