#!/usr/bin/python3
"""
Module for finding solutions to the N queens problem.
"""
import sys


solutions = []  # A list to store all possible solutions to the N queens problem
n = 0  # Size of the chessboard
positions = None  # A list of all possible positions on the chessboard


def get_input():
    """
    Retrieves and validates the program's argument.
    Returns:
        int: The size of the chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos1, pos2):
    """
    Check if two queens are in an attacking position.
    Args:
        pos1 (list or tuple): Position of the first queen.
        pos2 (list or tuple): Position of the second queen.
    Returns:
        bool: True if the queens are in an attacking position, otherwise False.
    """
    if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
        return True
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def group_exists(group):
    """
    Checks if a group of positions exists in the list of solutions.
    Args:
        group (list of lists of integers): A group of possible positions.
    Returns:
        bool: True if the group exists, otherwise False.
    """
    global solutions
    for sol in solutions:
        i = 0
        for sol_pos in sol:
            for grp_pos in group:
                if sol_pos[0] == grp_pos[0] and sol_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """
    Builds a solution for the N queens problem recursively.
    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions, n, positions
    if row == n:
        tmp = group.copy()
        if not group_exists(tmp):
            solutions.append(tmp)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([positions[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(positions[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets the solutions for the given chessboard size."""
    global positions, n
    positions = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    row = 0
    group = []
    build_solution(row, group)


n = get_input()
get_solutions()

"""Print all solutions"""
for solution in solutions:
    print(solution)
