# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import math


height_weight_age = np.array([70, 170, 40])
grades = np.array([95, 80, 75, 62])

def book_vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_add(v, w):
    return np.add(v, w)
    
def book_vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]
    
def vector_subtract(v, w):
    return np.subtract(v, w)
    
def book_vector_sum(v):
    result = v[0]
    for i in v[1:]:
        result = vector_add(result, i)
    return result    
    
def vector_sum(v):
    return np.sum(v)
    
def book_scalar_multiply(c, v):
    return [c * v_i for v_i in v]
    
def scalar_multiply(c, v):
    return np.multiply(c, v)
    
def book_vector_mean(v):
    n = len(v)
    return scalar_multiply(1/n, vector_sum(v))
    
def vector_mean(v):
    return np.average(v)
    
def book_dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])
    
def dot(v, w):
    return np.dot(v, w)
    
def sum_of_squares(v):
    return np.dot(v, v)
    
def book_magnitude(v):
    return math.sqrt(sum_of_squares(v))
    
def magnitude(v):
    return np.linalg.norm(v)
    
def book_distance(v, w):
    return magnitude(vector_subtract(v, w))
    
def distance(v, w):
    return np.linalg.norm(np.subtract(v, w))
    
A = np.matrix([[1, 2, 3], [4, 5, 6]])
B = np.matrix([[1, 2], [3, 4], [5, 6]])

def book_shape(A):
    rows = len(A)
    cols = len(A[0]) if A else 0
    return rows, cols

def shape(A):
    return np.shape(A)
    
def get_row(A, i):
    return A[i]
    
def book_get_column(A, j):
    return [A_i[j] for A_i in A]
    
def get_column(A, j):
    return A[:,j]
    
def make_matrix(rows, cols, fn):
    return np.matrix(
    [[fn(i, j) for j in range(cols)] for i in range(rows)] )
    
def is_diagonal(i, j):
    return 1 if i == j else 0
    
book_identity_matrix = make_matrix(5, 5, is_diagonal)
    
identity_matrix = np.identity(5)

def main():
    v = np.array([1, 2, 3, 4])
    w = np.array([10, 11, 12, 13])
    
    print('v', v)
    print('w', w)
    print('add', vector_add(v, w))
    print('subtract', vector_subtract(v, w))
    print('sum', vector_sum(v))
    print('multiply', scalar_multiply(2, v))
    print('mean', vector_mean(v))
    print('dot', dot(v, w))
    print('sum of squares', sum_of_squares(v))
    print('magnitude', magnitude(v))
    print('distance', distance(v, w))
    print('shape A', shape(A))
    print('get row A1', get_row(A, 1))
    print('get column A1', get_column(A, 1))
    print(make_matrix(5, 5, is_diagonal))
    

main()
    