#!/usr/bin/python3
"""
defines triangle module
"""


def pascal_triangle(n):
    """
    Defines pasacal triangle that create list of lists
    """
    def factorial(n):
        """
        finds factorial of a value
        """
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    MyList = []

    for i in range(0, n):
        row = []
        for j in range(0, i + 1):
            c = factorial(i) // (factorial(i - j) * factorial(j))
            row.append(c)

        MyList.append(row)

    return MyList
