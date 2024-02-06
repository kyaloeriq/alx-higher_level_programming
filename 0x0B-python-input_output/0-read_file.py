#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    the with statement must be used
    no need to manage file permission or file doesn't exist exceptions
    """
    with open(filename, encoding="utf-8") as j:
        read_data = j.read().rstrip()
        print(read_data)


if __name__ == "__main__":
    read_file("my_file_0.txt")
