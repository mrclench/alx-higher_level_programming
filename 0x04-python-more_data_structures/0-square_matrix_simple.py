#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """This function computes the square value of integers"""
    return list(map(lambda x:list(map(lambda y: (y**2), x)), matrix))
