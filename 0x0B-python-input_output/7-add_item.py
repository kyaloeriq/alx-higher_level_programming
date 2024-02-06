#!/usr/bin/python3
"""Load, add and save module"""
import os
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(filename, *args):
    """
    script that adds all arguments to a Python list,
    then save them to a file
    """
    my_list = load_from_json_file(filename) if os.path.exists(filename) else []
    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    filename = "add_item.json"
    items = sys.argv[1:]
    add_item(filename, *items)
