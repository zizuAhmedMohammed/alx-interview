#!/usr/bin/python3
"""Interview challenge Pascal Triangle"""


def pascal_triangle(n):
    """
    Return an empty list if n <= 0
    """
    if n <= 0:
        return []

    """ 
    Create a list to hold the triangle
    """
    triangle = [[1]]

    """ 
    Loop over each row of the triangle, adding the next row based on the previous row
    """
    for i in range(1, n):
        previous_row = triangle[i - 1]
        current_row = [1]
        for j in range(1, i):
            current_row.append(previous_row[j - 1] + previous_row[j])
        current_row.append(1)
        triangle.append(current_row)

    """ 
    Return the completed triangle
    """
    return triangle
