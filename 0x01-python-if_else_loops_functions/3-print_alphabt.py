#!/usr/bin/python3
for value in range(ord('a'), ord('z') + 1):
    if chr(value) in 'qe':
        continue
    print("{}".format(chr(value)), end='')
