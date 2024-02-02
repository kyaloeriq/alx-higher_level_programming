#!/usr/bin/python3
"""Module for function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices
    m_a and m_b must be an list of lists of integers or floats
    if m_a or m_b is not a list, a TypeError exception is raised
    if m_a or m_b is not a list of lists, a TypeError exception is raised
    if m_a or m_b is empty, a TypeError exception is raised
    if one element of those list of lists is not an integer or a float, a TypeError exception is raised
    if m_a or m_b is not a rectangle, a TypeError exception is raised
    If m_a and m_b can’t be multiplied, a ValueError exception is raised
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) != 1:
        raise ValueError("each row of m_b must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise ValueError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for a in range(len(m_a)):
        for b in range(len(m_b[0])):
            for c in range(len(m_b)):
                result[a][b] += m_a[a][c] * m_b[c][b]

    return result


if __name__ == "__main__":
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
