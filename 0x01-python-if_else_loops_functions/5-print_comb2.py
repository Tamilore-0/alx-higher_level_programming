#!/usr/bin/python3
# prints numbers in double digits
for number in range(0, 100):
    print("{:02d}".format(number), end="")
    if number < 99:
        print(", ", end="")
# new line
print()
