#!/usr/bin/python3
"""Interview challenge Pascal Triangle"""


def pascal_triangle(n):
    """returns a list of lists of numbers 
    representing the pascal triangle"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        """Loop over each row of the triangle, 
        adding the next row based on the previous row"""
        previous_row = triangle[i - 1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(previous_row[j - 1] + previous_row[j])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
