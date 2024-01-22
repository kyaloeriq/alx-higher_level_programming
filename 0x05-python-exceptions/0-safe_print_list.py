#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    while x < len(my_list):
        try:
            if my_list[x] is not None:
                print(my_list[x], end=" ")
                count += 1
        except IndexError:
            print()
            break
        x += 1
    print()  # Add a new line after printing all elements
    return count


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
