#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:30:13 2023
name: Yusen Wu
Email: wuyusen@bu.edu
Assigment: 4
File Description: Contains a sets of functions to for basic linear algebra manipulation(2D-list), 
including print_matrix, zeros, identity matrix, transpose, swap_rows, mult_row_scalar, add_row_into
"""

def print_matrix(A, label = ''):
  """
  takes two parameters, m which is a 2-dimension list 
  (the matrix) and label (a string), and creates a 
  nicely-formatted printout
  """
  if label != '':
    print(f'{label} = ')
  print(f'[', end = '')
  #Loop over each row in matrix and print it out
  for i,row in enumerate(A):
    if i != 0:
      print(' ', end = '')
    if i < len(A) - 1:
      print('[' + ', '.join([f'{num:.2f}' for num in row]) + ']')
    if i == len(A) - 1:
      print('[' + ', '.join([f'{num:.2f}' for num in row]) + ']]')

def zeros(n, m = None):
  """
  creates and returns an n * m matrix containing all zeros
  """
  if m == None:
    matrix = [[0 for _ in range(n)] for _ in range(n)]
  else:
    matrix = [[0 for _ in range(m)] for _ in range(n)]
  return matrix

def identity_matrix(n):
  """
  creates and returns an n * n identity matrix containing the 
  value of 1 along the diagonal
  """
  return [[1 if col == row else 0 for col in range(n)] for row in range(n)]

def transpose(M):
  """
  creates and returns the transpose of a matrix
  """
  rows = len(M[0])
  cols = len(M)
  #switch over col and row number
  return [[M[col][row] for col in range(cols)] for row in range(rows)]

def swap_rows(M, src, dest):
  """
  perform the elementary row operation that exchanges 
  two rows within the matrix
  """
  A = [1,2,3]
  assert src <= len(M) - 1, f"original index outbound"
  assert dest <= len(M) - 1, f"destination index outbound"
  M[src], M[dest] = M[dest], M[src]

def mult_row_scalar(M, row, scalar):
  """
  perform the elementary row operation that multiplies 
  all values in the row row by the numerical value scalar
  """
  assert row <= len(M) - 1, f"row index outbound"
  M[row] = [scalar*col for col in M[row]]

def add_row_into(M, src, dest):
  """
  performs the elementary-row operation to add the src 
  row into the dest row
  """
  assert src <= len(M) - 1, f"original index outbound"
  assert dest <= len(M) - 1, f"destination index outbound"
  M[dest] = [M[src][col] + M[dest][col] for col in range(len(M[0]))]
  