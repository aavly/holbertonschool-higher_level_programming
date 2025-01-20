#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in range(len(row)):
            print("{}".format(row[j]), end=' ' if j < len(row) - 1 else "")
        print()
