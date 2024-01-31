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

    def is_safe(board, row, col):
        """
        Check if it's safe to place a queen at board[row][col]
        """
        # Check the row on the left side
        for a in range(col):
            if board[row][a] == 1:
                return False

        # Check upper diagonal on the left side
        for a, b in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[a][b] == 1:
                return False

        # Check lower diagonal on the left side
        for a, b in zip(range(row, N, 1), range(col, -1, -1)):
            if board[a][b] == 1:
                return False

        return True

    def solve_nqueens_util(board, col):
        """
        Use backtracking to place queens recursively
        """
        # Base case: If all queens are placed, return True
        if col >= N:
            print_solution(board)
            return True

        # Consider this column and try placing a queen in all rows one by one
        for a in range(N):
            if is_safe(board, a, col):
                # Place this queen in board[a][col]
                board[a][col] = 1

                # Recur to place the rest of the queens
                solve_nqueens_util(board, col + 1)

                # If placing queen in board[a][col] doesn't lead to a solution,
                # then remove the queen from board[a][col]
                board[a][col] = 0

        # If queen can not be placed in row in this column col
        return False

    def print_solution(board):
        """
        Print the board configuration
        """
        for a in range(N):
            for b in range(N):
                print(board[a][b], end=" ")
            print()

        print()

    # Initialize the board with all 0s
    board = [[0] * N for _ in range(N)]

    # Call the recursive utility function to solve N queens problem
    solve_nqueens_util(board, 0)


if __name__ == "__main__":  # Command-line argument handling
    if len(sys.argv) != 2:
        print("Usage: python3 filename.py N", file=sys.stderr)
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
