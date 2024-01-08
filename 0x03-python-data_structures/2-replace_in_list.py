#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return my_list
    for i, value in enumerate(my_list):
        if i == idx:
            my_list[i] = element
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
