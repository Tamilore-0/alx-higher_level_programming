#!/usr/bin/python3
"""
A matrix module
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

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
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(sublist, list) for sublist in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(sublist, list) for sublist in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    if not all(
        isinstance(element, (int, float))
        for sublist in m_a for element in sublist
    ):
        raise TypeError("m_a should contain only integers or floats")
    if not all(
        isinstance(element, (int, float))
        for sublist in m_b for element in sublist
    ):
        raise TypeError("m_b should contain only integers or floats")

    if any(
        isinstance(element, (bool))
        for sublist in m_a for element in sublist
    ):
        raise TypeError("m_a should contain only integers or floats")
    if any(
        isinstance(element, (bool))
        for sublist in m_b for element in sublist
    ):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(sublist) != len(m_a[0]) for sublist in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(sublist) != len(m_b[0]) for sublist in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = list([0 for i in range(len(m_b[0]))] for j in range(len(m_a)))
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]
    return new_matrix
