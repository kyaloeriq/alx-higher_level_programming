#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        return max(my_list)
    else:
        return None


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
