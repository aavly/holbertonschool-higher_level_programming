#!/usr/bin/python3
"""
12. Pascal's Triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    list_of_numbers = [[1]]

    for i in range(1, n):
        row = [1]

        # accounting for middle values
        last_row = list_of_numbers[i - 1]
        for ii in range (len(last_row) - 1):
            row.append(last_row[ii] + last_row[ii + 1])

        row.append(1)
        list_of_numbers.append(row)

        return list_of_numbers
