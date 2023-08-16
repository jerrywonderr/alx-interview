#!/usr/bin/python3
"""Simple program to rotate a n x n 2D matrix"""


def rotate_2d_matrix(matrix):
    """This function rotates a matrix"""
    matrix_length = len(matrix)

    # Transpose the matrix
    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(matrix_length):
        matrix[i].reverse()
