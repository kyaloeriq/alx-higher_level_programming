#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    if 0 <= idx < len(my_list):
        new_list = my_list.copy()  # Copy to avoid modification of the original
        new_list[idx] = element
        return new_list
    else:
        return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
