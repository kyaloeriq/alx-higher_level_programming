#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():

    a = 10
    b = 5

    # Call functions with variables as arguments
    sum_rslt = add(a, b)
    diff_rslt = sub(a, b)
    mul_rslt = mul(a, b)
    div_rslt = div(a, b)

    # Print the results
    print("{} + {} = {}".format(a, b, sum_rslt))
    print("{} - {} = {}".format(a, b, diff_rslt))
    print("{} * {} = {}".format(a, b, mul_rslt))
    print("{} / {} = {}".format(a, b, div_rslt))


if __name__ == "__main__":
    main()
