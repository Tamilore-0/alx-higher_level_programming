#!/usr/bin/python3
"""
Matrix module
"""

import numpy as ny


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
    - m_a (list): The first matrix.
    - m_b (list): The second matrix.

    Returns:
    - list: The result of the matrix multiplication.

    Raises:
    - TypeError: If inputs are not valid matrices.
    - ValueError: If matrices cannot be multiplied.

    """
    if type(m_a) is not list:
        raise TypeError("m_a should be a list")
    if type(m_b) is not list:
        raise TypeError("m_b should be a list")

    if not all(isinstance(sublist, list) for sublist in m_a):
        raise TypeError("m_a should be a list of lists")
    if not all(isinstance(sublist, list) for sublist in m_b):
        raise TypeError("m_b should be a list of lists")

    if not m_a or not m_a[0]:
        raise ValueError("m_a musn't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b musn't be empty")

    if not all(
        isinstance(element, (int, float))
        for sublist in m_a for element in sublist
    ):
        raise TypeError("m_a must contain only integers or floats")
    if not all(
        isinstance(element, (int, float))
        for sublist in m_b for element in sublist
    ):
        raise TypeError("m_b must contain only integers or floats")

    if any(
        isinstance(element, (bool))
        for sublist in m_a for element in sublist
    ):
        raise TypeError("m_a must contain only integers or floats")
    if any(
        isinstance(element, (bool))
        for sublist in m_b for element in sublist
    ):
        raise TypeError("m_b must contain only integers or floats")

    if any(len(sublist) != len(m_a[0]) for sublist in m_a):
        raise TypeError("each row of m_a must be the same size")
    if any(len(sublist) != len(m_b[0]) for sublist in m_b):
        raise TypeError("each row of m_b must be the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("Matrices cannot be multiplied")

    result = ny.dot(m_a, m_b)
    return result
