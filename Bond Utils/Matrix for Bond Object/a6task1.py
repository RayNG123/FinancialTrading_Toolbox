#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 6
#File Description: This file contains conde for a user defined class Matrix, 
#and a set of functions to to print out and process related statistics. The
#user can also perform a series of basica matrix operation including addtion,
#subtraction, dot product

import random

class Matrix:
  """
  A user defined class object of a 2-dimensional matrix.
  The matrix will support a wide-variety of operations, 
  including printing itself out, row-based operations, 
  and some linear-algebra operations.
  """
  def __init__(self,matrix):
    """
    initiate a matrix object requires a 2D list containing
    all data of the matrix
    """
    self.__matrix = matrix

  def __repr__(self):
    """
    A nicely fomatted textual representation of the matrix
    """
    repr = '['

    #Iterate over and print each row 
    for i,row in enumerate(self.__matrix):
      if i > 0:
        repr += ' '

      #sum up elements
      repr += '[' + ', '.join([f'{num:.2f}' for num in row]) + ']'
      if i != len(self.__matrix) - 1:
        repr += '\n'

    repr += ']'
    return repr

  def describe(self):
    """
    returns a string containing some useful descriptive information about 
    the values in a Matrix
    """
    repr = self.__repr__()
    repr += '\n'

    #print dimensions
    repr += f'dimensions: {len(self.__matrix)} X {len(self.__matrix[0])}'
    repr += '\n'

    #print sum of elements
    repr += f'sum of elements: {sum([num for row in self.__matrix for num in row])}'
    repr += '\n'

    #print mean of elements
    repr += f'mean of elements: {sum([num for row in self.__matrix for num in row])/(len(self.__matrix)*len(self.__matrix[0]))}'
    repr += '\n'

    #print column sums
    repr += f'column sums: {[sum(col) for col in self.transpose().__matrix]}'
    repr += '\n'

    #print column means
    repr += f'column means: {[sum(col)/len(col) for col in self.transpose().__matrix]}'
    repr += '\n'

    return repr

  def __eq__(self, other):
    """
    Self defined euqality test bewteen different matrix object
    """
    #check data type
    if type(self) != type(other):
      return False

    #check dimensions
    if (len(self.__matrix) != len(other.__matrix)) or (len(self.__matrix[0]) != len(other.__matrix[0])):
      return False

    #Iterate over each element to check if euqal in both Matrixs
    for row in range(len(self.__matrix)):
      for col in range(len(self.__matrix[0])):
        if self.__matrix[row][col] != other.__matrix[row][col]:
          return False
    return True

  def add_row_into(self, src, dest):
    """
    performs the elementary-row operation to add the src 
    row into the dest row
    """
    assert src <= len(self.__matrix) - 1, f"original index outbound"
    assert dest <= len(self.__matrix) - 1, f"destination index outbound"

    self.__matrix[dest] = [self.__matrix[src][col] + self.__matrix[dest][col] for col in range(len(self.__matrix[0]))]

  def add_mult_row_into(self, scalar, src, dest):
    """
    performs the elementary-row operation to add the a scalar times 
    src row into the dest row
    """
    assert src <= len(self.__matrix) - 1, f"original index outbound"
    assert dest <= len(self.__matrix) - 1, f"destination index outbound"

    self.__matrix[dest] = [scalar*self.__matrix[src][col] + self.__matrix[dest][col] for col in range(len(self.__matrix[0]))]

  def swap_rows(self, src, dest):
    """
    perform the elementary row operation that exchanges 
    two rows within the matrix
    """
    assert src <= len(self.__matrix) - 1, f"original index outbound"
    assert dest <= len(self.__matrix) - 1, f"destination index outbound"

    self.__matrix[src], self.__matrix[dest] = self.__matrix[dest], self.__matrix[src]

  def add_scalar(self, scalar):
    """
    return a new matrix object that is poinwisely scalar 
    added on the orignal matrix
    """
    assert(isinstance(scalar,(int,float))), f'wrong data type'
    return Matrix([[scalar + col for col in row] for row in self.__matrix])

  def mult_scalar(self, scalar):
    """
    return a new matrix object that is poinwisely scalar 
    multiplied on the orignal matrix
    """
    assert(isinstance(scalar,(int,float))), f'wrong data type'
    return Matrix([[scalar*col for col in row] for row in self.__matrix])

  def add_matrices(self, other):
    """
    takes as parameters 2 matrices (2d lists) and returns 
    a new matrix which is the element-wise sum of the matrices 
    A and B
    """
    assert len(self.__matrix) == len(other.__matrix), f'incompatible dimensions: cannot add ({len(self.__matrix)},{len(self.__matrix[0])}) with ({len(other.__matrix)},{len(other.__matrix[0])})!'
    assert len(self.__matrix[0]) == len(other.__matrix[0]), f'incompatible dimensions: cannot add ({len(self.__matrix)},{len(self.__matrix[0])}) with ({len(other.__matrix)},{len(other.__matrix[0])})!'
    
    return Matrix([[self.__matrix[row][col] + other.__matrix[row][col] for col in range(len(self.__matrix[0]))] for row in range(len(other.__matrix))])

  def __add__(self, scalar):
    """
    return a new matrix object that is poinwisely scalar 
    added on the orignal matrix or matrix addition
    """
    assert(isinstance(scalar,(int,float,Matrix))), f'only matrix, int, float data type is supported'

    #check for matrix addtion or scalar addtion
    if isinstance(scalar, Matrix):
      return self.add_matrices(scalar)
    else:
      return self.add_scalar(scalar)

  def __sub__(self, scalar):
    """
    return a new matrix object that is poinwisely scalar 
    minused on the orignal matrix or matrix subtraction
    """
    assert(isinstance(scalar,(int,float,Matrix))), f'only matrix, int, float data type is supported'

    #check for matrix subtraction or scalar subtraction
    if isinstance(scalar, Matrix):
      return self.add_matrices(scalar.mult_scalar(-1))
    else:
      return self.add_scalar(-scalar)

  def __mul__(self, scalar):
    """
    return a new matrix object that is poinwisely scalar 
    multiplied on the orignal matrix or matrix dot product
    """
    assert(isinstance(scalar,(int,float,Matrix))), f'only matrix, int, float data type is supported'

    #check for matrix multiplication or scalar multiplication
    if isinstance(scalar,Matrix):
      return self.dot_product(scalar)
    else:
      return self.mult_scalar(scalar)
  
  def __truediv__(self, scalar):
    """
    return a new matrix object that is poinwisely scalar 
    divided on the orignal matrix
    """
    assert isinstance(scalar,(int,float)),f'unsupported data type'
    return self.mult_scalar(1/scalar)

  def transpose(self):
    """
    creates and returns the transpose of itself
    """
    rows = len(self.__matrix[0])
    cols = len(self.__matrix)

    #switch over col and row number
    return Matrix([[self.__matrix[col][row] for col in range(cols)] for row in range(rows)])

  def dot_product(self, other):
    """
    takes as parameters two matrices M and N, and 
    returns a new matrix containing dot product 
    of these matrices
    """
    assert len(self.__matrix[0]) == len(other.__matrix), f'incompatible dimensions: cannot dot product ({len(self.__matrix)},{len(self.__matrix[0])}) with ({len(other.__matrix)},{len(other.__matrix[0])})!'
    
    #Iniatiate a data container
    matrix = [[0 for _ in other.__matrix[0]] for _ in self.__matrix]
    other_T = other.transpose()

    #Loop over each row and col of final matrix: matrix[row][col] is dot product of A[row]*B_T[col]
    for row in range(len(matrix)):
      for col in range(len(matrix[0])):
        matrix[row][col] = sum([self.__matrix[row][i] * other_T.__matrix[col][i] for i in range(len(self.__matrix[0]))])
    return Matrix(matrix)

  @classmethod
  def zeros(Matrix, row, col = None):
    """
    return a matrix that is filled by zeros
    """
    #check for column specification
    if col == None:
      return Matrix([[0 for _ in range(row)] for _ in range(row)])
    else:
      return Matrix([[0 for _ in range(col)] for _ in range(row)])

  @classmethod
  def ones(Matrix, row, col = None):
    """
    return a matrix that is filled by ones
    """
    #check for column specification
    if col == None:
      return Matrix([[1 for _ in range(row)] for _ in range(row)])
    else:
      return Matrix([[1 for _ in range(col)] for _ in range(row)])
  
  @classmethod
  def identity(Matrix, n):
    """
    return an identity matrix accoding to the specification
    """
    return Matrix([[1 if col == row else 0 for col in range(n)] for row in range(n)])

  @classmethod
  def random_int_matrix(Matrix, row, col = None, low = 1, high = 10):
    """
    draw a row*col matrix of random integers in the range of low to high
    """
    #check for column specification and draw random numbers
    if col == None:
      return Matrix([[random.randint(low, high) for _ in range(row)] for _ in range(row)])
    else:
      return Matrix([[random.randint(low, high) for _ in range(col)] for _ in range(row)])
  
  @classmethod
  def random_float_matrix(Matrix, row, col = None, low = 0, high = 1):
    """
    draw a row*col matrix of random floats in the range of low to high
    """
    #check for column specification and draw random numbers
    if col == None:
      return Matrix([[random.uniform(low, high) for _ in range(row)] for _ in range(row)])
    else:
      return Matrix([[random.uniform(low, high) for _ in range(col)] for _ in range(row)])