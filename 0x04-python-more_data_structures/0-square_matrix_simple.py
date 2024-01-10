#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newmatrix = []
    for row in matrix:
        newrow = []
        for i in row:
            newrow.append(i ** 2)
        newmatrix.append(newrow)
    return newmatrix
