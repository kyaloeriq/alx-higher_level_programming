#!/usr/bin/python3
"""Module that prints a square with the character #"""


def print_square(size):
    """
    function that prints a square with the character #
    Parameters:
    - size (int): The size length of the square.
    size must be an integer, otherwise a TypeError is raised
    if size is less than 0, ValueError exception is raised
    if size is a float and is less than 0, TypeError exception is raised
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
