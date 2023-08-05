#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 7
#File Description: This file contains a set of functions print a option pricing table
#and a

import math

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

def get_binomial_factors(sigma, rf, div, h):
    """
    calculates the factors needed to implement the binomial calculations 
    """
    u = math.exp((rf - div)*h + sigma*h**(1/2))
    d = math.exp((rf - div)*h - sigma*h**(1/2))
    return u, d

def get_risk_neutral_probability(sigma, rf, div, h):
    """
    calculates and returns the risk-neutral probability associated with 
    this option’s parameters
    """
    u, d = get_binomial_factors(sigma, rf, div, h)
    return (math.exp((rf - div)*h) - d)/(u - d)

def build_binomial_stock_price_tree(s, sigma, rf, div, T, n):
    """
    builds and returns a binomial tree (a 2-d list) of simulated stock 
    price movements
    """
    #Get binomial factors needed and length of tree
    u, d = get_binomial_factors(sigma, rf, div, T/n)
    periods = int(n) + 1

    #Ierate over each tree node to set the price of the tree
    tree = []
    for i in range(periods):
      price_list = [s*(u**(j - i))*(d**(i)) if j >= i else 0 for j in range(periods)]
      tree.append(price_list)
    return tree

def print_binomial_tree(tree):
    """
    takes a single parameter (a 2-dimension list) which containts the 
    data of the binomial tree, and creates a nicely-formatted printout
    """
    for i,tri in enumerate(tree):
      print(' '*8*i + ' '.join([f'{tr:>7.2f}' for tr in tri][i:len(tri)]))