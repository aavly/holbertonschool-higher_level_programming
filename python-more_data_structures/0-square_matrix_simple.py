#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
	new_matrix = list(map(lambda row : list(map(lambda x : x ** 2, row)), matrix))
	return new_matrix

    #square_matrix = [row[:] for row in matrix]

    #for i in range(len(square_matrix)):
        #for j in range(len(square_matrix[i])):
            #square_matrix[i][j] = square_matrix[i][j] ** 2

    #return square_matrix
