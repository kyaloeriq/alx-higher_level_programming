#!/usr/bin/python3
import sys


def main():

    argc = len(sys.argv)
    argp = sys.argv

    # print the number of and list of arguments
    if argc == 1:
        print(f"{argc - 1} argument.")
    elif argc > 1:
        print(f"{argc - 1} arguments:\n{argp[1:]}")


if __name__ == "__main__":
    main()
