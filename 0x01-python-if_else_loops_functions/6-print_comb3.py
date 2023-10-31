#!/usr/bin/python3
for x in range(0, 10):
    for y in range (x, 10):
        if y == x:
            continue
        print("{}{}, ".format(x, y), end='')
# new line
print()