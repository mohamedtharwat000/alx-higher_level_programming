#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            if column == row[len(row) - 1]:
                print("{0:d}".format(column))
            else:
                print("{0:d}".format(column), end=" ")
