#!/usr/bin/python3
def uppercase(str):
    result = ''
    for letter in str:
        if 'a' <= letter <= 'z':
            result += chr(ord(letter) - 32)
        else:
            result += letter
    print("{}".format(result))
