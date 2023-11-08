#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    update_data = {key: value}
    a_dictionary_copy = a_dictionary.copy()
    for keys, item in a_dictionary_copy.items():
        if key in a_dictionary:
            if value == item:
                continue
            else:
                a_dictionary[key] = value
        else:
            a_dictionary.update(update_data)
    return a_dictionary
