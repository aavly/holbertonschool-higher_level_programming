#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = [row[:] for row in matrix]

    for i in range(len(square_matrix)):
        for j in range(len(square_matrix)):
            square_matrix[i][j] = square_matrix[i][j] ** 2

    return square_matrix
