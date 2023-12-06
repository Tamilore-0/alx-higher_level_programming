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

    for i in range(0, n + 1):
        row = []
        for j in range(0, i + 1):
            c = factorial(i) // (factorial(i - j) * factorial(j))
            row.append(c)

        MyList.append(row)

    return MyList

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


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))