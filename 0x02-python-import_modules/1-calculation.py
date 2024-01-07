#!/usr/bin/python3
import calculator_1 as my_module


def main():

    a = 10
    b = 5

    # Import specific functions from my_module
    add_function = my_module.add
    sub_function = my_module.sub
    mul_function = my_module.mul
    div_function = my_module.div

    # Call functions with variables as arguments
    sum_rslt = add_function(a, b)
    diff_rslt = sub_function(a, b)
    mul_rslt = mul_function(a, b)
    div_rslt = div_function(a, b)

    # Print the results
    print("{} + {} = {}".format(a, b, sum_rslt))
    print("{} - {} = {}".format(a, b, diff_rslt))
    print("{} * {} = {}".format(a, b, mul_rslt))
    print("{} / {} = {}".format(a, b, div_rslt))


if __name__ == "__main__":
    main()
