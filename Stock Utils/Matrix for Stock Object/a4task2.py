#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:30:20 2023
name: Yusen Wu
Email: wuyusen@bu.edu
Assigment: 4
File Description: Contains a sets of functions to for basic linear algebra manipulation(2D-list), 
including add_matrices, mult_scalar, sub_matrices, element_product, dot_product, create_sub_matrix, 
determinant, matrix of minors, inverse matrix
"""
from a4task1 import *

def add_matrices(A, B):
  """
  takes as parameters 2 matrices (2d lists) and returns 
  a new matrix which is the element-wise sum of the matrices 
  A and B
  """
  assert len(A) == len(B), f'incompatible dimensions: cannot add ({len(A)},{len(A[0])}) with ({len(B)},{len(B[0])})!'
  assert len(A[0]) == len(B[0]), f'incompatible dimensions: cannot add ({len(A)},{len(A[0])}) with ({len(B)},{len(B[0])})!'
  return [[A[row][col] + B[row][col] for col in range(len(A[0]))] for row in range(len(A))]

def mult_scalar(M, s):
  """
  takes as a parameter a 2-dimension list M (the matrix) 
  and a scalar value s (i.e., an int or float), and returns 
  a new matrix containing the values of the original matrix 
  multiplied by the scalar value.
  """
  return [[s*M[row][col] for col in range(len(M[0]))] for row in range(len(M))]

def sub_matrices(A, B):
  """
  takes as parameters 2 matrices (2d lists) and returns a 
  new matrix which is the element-wise difference of the 
  matrices A and B.
  """
  assert len(A) == len(B), f'incompatible dimensions: cannot subtract ({len(A)},{len(A[0])}) with ({len(B)},{len(B[0])})!'
  assert len(A[0]) == len(B[0]), f'incompatible dimensions: cannot subtract ({len(A)},{len(A[0])}) with ({len(B)},{len(B[0])})!'
  return add_matrices(A, mult_scalar(B, -1))

def element_product(A, B):
  """
  takes as parameters two matrices A and B, and 
  returns a new matrix containing element-wise 
  product of these matrices.
  """
  assert len(A) == len(B), f'incompatible row dimensions: {len(A)} != {len(B)}'
  return [[A[row][col] * B[row][col] for col in range(len(A[0]))] for row in range(len(A))]

def dot_product(A, B):
  """
  takes as parameters two matrices M and N, and 
  returns a new matrix containing dot product 
  of these matrices
  """
  assert len(A[0]) == len(B), f'incompatible dimensions: cannot dot product ({len(A)},{len(A[0])}) with ({len(B)},{len(B[0])})!'
  matrix = zeros(len(A),len(B[0]))
  B_T = transpose(B)
  #Loop over each row and col of final matrix: matrix[row][col] is dot product of A[row]*B_T[col]
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      matrix[row][col] = sum([A[row][i] * B_T[col][i] for i in range(len(A[0]))])
  return matrix

def create_sub_matrix(M, exclude_row, exclude_col):
  """
  returns a sub-matrix of M, with all values that 
  are not in row exclude_row or column exclude_col
  """
  assert exclude_row <= len(M) - 1, f"row index outbound"
  assert exclude_col <= len(M[0]) - 1, f"col index outbound"
  return [[M[row][col] for col in range(len(M[0])) if col != exclude_col] for row in range(len(M)) if row != exclude_row]

def determinant(M):
  """
  takes a parameter M that is a (non-singular) matrix, 
  and returns its determinant.
  """
  assert len(M) == len(M[0]), f'cannot find determinant of shape ({len(M)},{len(M[0])})!'
  #return only number of matrix has only one row and one col
  if len(M) == 1:
    return M[0][0]
  #return cross product of matrix has only two row and two col
  elif len(M) == 2:
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]
  #else return sum of determinant of smaller matrixs
  else:
    matrixs = [create_sub_matrix(M,0,i) for i in range(len(M[0]))]
    coefficient_1 = [(-1)**i for i in range(len(M[0]))]
    coefficient_2 = M[0]
    return sum([determinant(matrix)*coefficient_1[i]*coefficient_2[i] for i,matrix in enumerate(matrixs)])

def matrix_of_minors(M):
  """
  takes a matrix and returns the corresponding matrix of minors
  """
  assert len(M) == len(M[0]), f'cannot find matrix of minors for shape ({len(M)},{len(M[0])})!'
  matrix = zeros(len(M))
  #itertate over each row and col to get matrix of minors
  for row in range(len(M)):
    for col in range(len(M[0])):
      matrix[row][col] = determinant(create_sub_matrix(M,row,col))
  return matrix

def inverse_matrix(M):
  """
  takes a parameter that is a (non-singular) matrix, and returns 
  its inverse
  """
  assert len(M) == len(M[0]), f'cannot find inverse matrix of shape ({len(M)},{len(M[0])})!'
  #get determinants
  det = determinant(M)
  #get matrix of minors
  minors = matrix_of_minors(M)
  #get cofacters
  cofactors = [[(-1)**(col+row) for col in range(len(M[0]))] for row in range(len(M))]
  #element product cofactors and matrix of minors
  cofac_minor = element_product(minors, cofactors)
  #get transpose
  cofac_minor_T = transpose(cofac_minor)
  return mult_scalar(cofac_minor_T,1/det)
