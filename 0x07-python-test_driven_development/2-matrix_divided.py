#!/usr/bin/python3
"""
Divides all elements of a matrix by a given number
it is a list of lists of integers/floats, otherwise TypeError is raised
rows of matrix must be of the same size, otherwise TypeError is raised
div must be a number (integer or float), otherwise TypeError is raised
div can’t be equal to 0, otherwise ZeroDivisionError is raised
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    Arguments:
        matrix: Matrix to be divided
        div: Number to divide the matrix by
    """
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(num / div, 2) for num in row] for row in matrix]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
