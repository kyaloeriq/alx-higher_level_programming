#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    [print("{}".format(num)) for num in reversed(my_list)]


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
