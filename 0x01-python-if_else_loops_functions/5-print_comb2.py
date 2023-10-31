#!/usr/bin/python3
# prints numbers in double digits
for number in range(0, 100):
    if number == 99:
        print("{:02d}".format(number))
    else:
        print("{:02d}, ".format(number), end="")
