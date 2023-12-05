#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                end_space = ' ' if col != len(matrix[row]) - 1 else ''
                print("{:d}".format(matrix[row][col]), end=end_space)
            print()
