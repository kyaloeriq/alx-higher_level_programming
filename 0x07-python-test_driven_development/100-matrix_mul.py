#!/usr/bin/python3
"""Module for function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices
    m_a and m_b must be an list of lists of integers or floats
    """
    if not isinstance(m_a, list):
         raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
         raise TypeError("m_b must be a list")
    if m_a = []:
        raise ValueError("m_a can't be empty")
    if m_b = []:
        raise ValueError("m_b can't be empty")
    if m_a = [:] is not int or float:
        raise TypeError("m_a should contain only integers or floats")
    if m_b = [:] is not int or float:
        raise TypeError("m_b should contain only integers or floats")
    if not isinstance(sizeofrows(m_a) are equal:
         raise ValueError("each row of m_b must be of the same size")
    if not isinstance(sizeofrows(m_a) are equal:
         raise ValueError("each row of m_b must be of the same size"
    if (m_a * m_b == NULL):
        raise ValueError("m_a and m_b can't be multiplied")

    return (m_a * m_b)


if __name__ == "__main__":
    [[7, 10], [15, 22]]
    [[13, 16]]



