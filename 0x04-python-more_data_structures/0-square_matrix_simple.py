#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[num ** 2 for num in row] for row in matrix]
    return
    new_matrix = [row[:] for row in matrix]
    for idx, row in enumerate(new_matrix):
        for idx2, col in enumerate(new_matrix):
            new_matrix[idx][idx2] = row[idx2] ** 2
    return new_matrix 
 Binary file modifiedBIN -65 Bytes (90%)  
