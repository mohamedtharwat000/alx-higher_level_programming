#!/usr/bin/python3

"""
    module for function pascal_triangle.
"""


def pascal_triangle(n):
    """
        pascal_triangle - function that returns a list of lists of integers
        representing the Pascal's triangle of n.
        Args:
            n: number of rows of the triangle.
        Return:
            list of lists of integers, or None if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
