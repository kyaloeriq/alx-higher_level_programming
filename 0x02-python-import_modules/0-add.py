#!/usr/bin/python3
import add_0 as my_module


def main():
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, my_module.add(a, b)))


if __name__ == "__main__":
    main()
