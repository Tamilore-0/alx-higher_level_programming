#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x, 10):
        # ensures numbers are distinct
        if y == x:
            continue
        print("{}{}".format(x, y), end='')
        # ensures comma is not printed at the end
        if x < 8:
            print(", ", end="")
# new line
print()
