#!/usr/bin/python3
def no_c(my_string):
    string_cpy = ''
    for i in range(len(my_string)):
        if my_string[i] in 'cC':
            continue
        string_cpy += my_string[i]
    return string_cpy
