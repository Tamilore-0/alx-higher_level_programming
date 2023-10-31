#!/usr/bin/python3
for value in range(ord('z'), ord('a') - 1, -1):
    if value % 2 != 0:
        value -= 32
    print("{}".format(chr(value)), end='')
