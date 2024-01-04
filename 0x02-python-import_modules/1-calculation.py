#!/usr/bin/python3
import calculator_1 as my_module


def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, my_module.add(a, b)))
    print("{} - {} = {}".format(a, b, my_module.sub(a, b)))
    print("{} * {} = {}".format(a, b, my_module.mul(a, b)))
    print("{} / {} = {}".format(a, b, my_module.mul(a, b)))


if __name__ == "__main__":
    main()
