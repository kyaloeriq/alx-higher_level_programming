#!/usr/bin/python3
"""
Integers addition module
if a and b are not integers, TypeError exception is raised
"""


def add_integer(a, b=98):
    """function that adds 2 integers"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    """Cast to integers if float"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    """Return the sum as an integer"""
    return int(a + b)


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
