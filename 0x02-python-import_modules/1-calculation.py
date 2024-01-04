#!/usr/bin/python3
import calculator_1 as my_module


def main():
    a = 10
    b = 5
    sum_rslt = my_module.add(a, b)
    diff_rslt = my_module.sub(a, b)
    mul_rslt = my_module.mul(a, b)
    div_rslt = my_module.div(a, b)
    print("{} + {} = {}".format(a, b, sum_rslt))
    print("{} - {} = {}".format(a, b, diff_rslt))
    print("{} * {} = {}".format(a, b, mul_rslt))
    print("{} / {} = {}".format(a, b, div_rslt))


if __name__ == "__main__":
    main()
