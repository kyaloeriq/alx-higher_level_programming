#!/usr/bin/python3
"""Module for function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    returns the number of characters written
    the with statement should be used
    no need to manage file permission exceptions
    function should create the file if doesn’t exist
    function overwrites the content of the file if it already exists
    """
    with open(filename, mode="w", encoding="utf-8") as k:
        nb_characters_written = k.write(text)
        return nb_characters_written


if __name__ == "__main__":
    nb_characters = write_file(
            "my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
