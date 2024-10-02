#!/usr/bin/python3
"""
    a module that creates a pascal triangle using n which is how many rows
"""


def pascal_triangle(n):
    """Creates a list of lists of integers to represent pascal triagle

    Args:
        n (int): the number of rows
        i (int): number of rows
        j (int): number of chars in row(i)
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            elif i > 0 and j > 0:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
