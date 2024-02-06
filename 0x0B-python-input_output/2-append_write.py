#!/usr/bin/python3
"""Module for function that appends a string to a text file"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    returns the number of characters added
    the with statement should be used
    no need to manage file permission exceptions
    function should create the file if doesn’t exist
    """
    with open(filename, mode="a", encoding="utf-8") as k:
        nb_characters_added = k.write(text)
        return nb_characters_added


if __name__ == "__main__":
    nb_characters_added = append_write(
            "file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
