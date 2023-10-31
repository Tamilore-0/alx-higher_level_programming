#!/usr/bin/python3
for value in range(ord('a'), ord('z') + 1):
    if chr(value) in 'qe':
        continue
    print(chr(value), end='')
