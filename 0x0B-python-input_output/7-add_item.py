#!/usr/bin/python3
"""Load, add and save module"""
from save_to_json_file import save_to_json_file 
from load_from_json_file import load_from_json_file


def add_item(filename, *args):
    """
    script that adds all arguments to a Python list,
    then save them to a file
    """
    my_list = load_from_json_file
    my_list.extend(args)
    save_to_json_file(my_list, filename)
