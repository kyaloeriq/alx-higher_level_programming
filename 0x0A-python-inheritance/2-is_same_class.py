#!/usr/bin/python3
"""Module returns True if object is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class,
    otherwise False
    """
    return type(obj) is a_class


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
