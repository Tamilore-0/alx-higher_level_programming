#!/usr/bin/python3
def islower(c):
    for value in range(ord('a'), ord('z') + 1):
        if ord(c) == value:
            return True
        else:
            continue
