#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:30:20 2023
name: Yusen Wu
Email: wuyusen@bu.edu
Assigment: 4
File Description: contains a set of functions to reimplement calculations of some bond 
relatedmetrics: portfolio_return, bond_price, bond_duration, bootstrap
"""

from a4task1 import *
from a4task2 import *
from a2task1 import cashflow_times, bond_cashflows, discount_factors

def portfolio_return(weights, returns):
  """
  calculate and return the portfolio return for an investment portfolio
  """
  #test data type of  weights and return and transform accordingly
  if type(weights[0]) in [float,int]:
    weights = [weights]
  if type(returns[0]) in [float,int]:
    returns = [returns]
  assert len(weights) == len(returns),f'Incompatible shapes'
  return dot_product(weights, transpose(returns))[0][0]

def bond_price(fv, c, n, m, ytm):
  """
  calculate and return the price of a bond using linear algebra
  """
  #get cashflows and factors
  cashflows = [bond_cashflows(fv, c, n,m)]
  factors = [discount_factors(ytm, n, m)]
  assert len(cashflows[0]) == len(factors[0]), f'incompatible dimensions: cannot dot ({len(cashflows)},{len(cashflows[0])}) with ({len(factors[0])},{len(factors)})!'
  return float(dot_product(cashflows,transpose(factors))[0][0])

def bond_duration(fv, c, n, m, ytm):
  """
  calculate and return the annulized duration of a bond using 
  linear algebra
  """
  #get cashflows
  cashflows = [bond_cashflows(fv, c, n, m)]
  #get discount factors
  factors = [discount_factors(ytm, n, m)]
  #get discount factors
  times = [cashflow_times(n,m)]
  result = dot_product(element_product(cashflows,factors),transpose(times))
  price = bond_price(fv, c, n, m, ytm)
  return float(mult_scalar(result,1/price)[0][0])/m

def bootstrap(cashflows, prices):
  """
  implement the bootstrap method
  """
  CF_inverse = inverse_matrix(cashflows)
  return dot_product(CF_inverse,prices)




