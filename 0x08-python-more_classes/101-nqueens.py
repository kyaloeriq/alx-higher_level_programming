#!/usr/bin/python3
"""program that solves the N queens problem"""
import sys


def nqueens(N):
    """
    program that solves the N queens problem
    N must be an integer greater or equal to 4
    program should print every possible solution to the problem
    """
    if not isinstance(N, int):
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":  # Command-line argument handling
    if len(sys.argv) != 2:
        print("Usage: python3 filename.py N", file=sys.stderr)
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("Invalid value for N. N must be an integer.", file=sys.stderr)
        sys.exit(1)
