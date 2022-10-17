#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []

    for j in matrix:
        if not isinstance(j, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for i in j:
            if not (type(i) == int or type(list) == float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for x in range(len(matrix) - 1):
        if not len(matrix[x]) == len(matrix[x + 1]):
            raise TypeError('Each row of the matrix must have the same size')
    if not (type(div) == int or type(div) == float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        lists = []
        for y in row:
            z = round(y / div, 2)
            lists.append(z)
        new_matrix.append(lists)
    return new_matrix
