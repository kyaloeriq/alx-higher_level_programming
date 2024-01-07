#!/usr/bin/python3
import sys


def main():

    argc = len(sys.argv)
    argp = sys.argv

    # print the number of and list of arguments
    if argc == 1:
        print(f"0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print(f"1: {argp[1]}")
    elif argc > 1:
        print(f"{argc - 1} arguments:")
        for i in range(1, argc):
            print(f"{i}: {argp[i]}")


if __name__ == "__main__":
    main()
