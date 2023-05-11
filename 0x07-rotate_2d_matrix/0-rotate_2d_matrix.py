#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """ Rotates a 2D matrix by 90 degrees clockwise
    Given an n x n 2D matrix, this function rotates it 90 degrees clockwise.
    Args:
    matrix: A 2D list representing the matrix to be rotated

    Returns:
    The rotated matrix as a 2D list.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i-1] = temp
