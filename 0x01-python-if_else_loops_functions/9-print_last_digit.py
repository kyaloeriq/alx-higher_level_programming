#!/usr/bin/python3
def print_last_digit(number):
    # Calculate the last digit of a given number
    lst_dgt = abs(number) % 10

    print("{:d}".format(lst_dgt), end='')

    return lst_dgt


if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
