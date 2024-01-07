#!/usr/bin/python3
import sys


def cstm_add(*args):
    return sum(args)


def main():

    num = [int(arg) for arg in sys.argv[1:]]
    rslt_sum = cstm_add(*num)

    print(rslt_sum)


if __name__ == "__main__":
    main()
