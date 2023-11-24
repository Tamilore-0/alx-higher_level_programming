#!/usr/bin/python3
"""
This module provides matrix_divided();
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix (list of lists) of integers or floats.
        div (int or float): The divisor for the division.

    Returns:
        list: A new matrix with each element rounded to two decimal places
              after dividing by the divisor.
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(_, list) for _ in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for _ in matrix:
        if not all(isinstance(i, (int, float)) for i in _):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if any(isinstance(j, bool) for j in _):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    for _ in matrix:
        if len(_) != len(matrix[0]):
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

    new_matrix = []
    for row in range(len(matrix)):
        new_matrix_row = []
        for i in range(len(matrix[row])):
            new_matrix_row.append(round(matrix[row][i] / div, 2))
        new_matrix.append(new_matrix_row)

    return new_matrix
