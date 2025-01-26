#!/usr/bin/python3
"""Divided matrix function"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    Each row of matrix must be of same size.

    Args:
        matrix: matrix (a list of lists) containing values to be divided.
        div: number (int or float) to divide numbers by.

    Returns:
        A new matrix with the elements divided by `div`,
        rounded to 2 decimal places.

    Raises:
        TypeError:  If a matrix is not a list of lists of integers/floats
                    If rows of the matrix are not of the same size
                    If 'div' is not a number
        ZeroDivisionError:  If 'div' is 0
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
