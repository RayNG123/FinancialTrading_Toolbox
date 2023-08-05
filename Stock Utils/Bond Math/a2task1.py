#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:47:07 2023
name: Yusen Wu
Email: wuyusen@bu.edu
Assigment: 1
"""

def cashflow_times(n, m):
  """
  develop the list of the times at which a bond makes 
  coupon payments, with n years and m coupon payments per year
  """
  return list(range(1, n*m +1))

def discount_factors(r, n, m):
  """
  calculate and return a list of discount factors for a given 
  annualized interest rate r, for n years, and m discounting 
  periods per year
  """
  return [1/(1 + r/m)**t for t in cashflow_times(n, m)]

def bond_cashflows(fv, c, n, m):
  """
  calculate and return a list of cashflows for a bond 
  specified by the parameters
  """
  cashflows = [fv*c/m for i in cashflow_times(n, m)]
  cashflows[-1] += fv
  return cashflows

def bond_price(fv, c, n, m, r):
  """
  calculate and return the price of a bond
  """
  cashflows = bond_cashflows(fv, c, n, m)
  discount = discount_factors(r, n, m)
  return sum([cashflows[i]*discount[i] for i in range(len(cashflows))])

def bond_yield_to_maturity(fv, c, n, m, price, accuracy = 0.0000001):
  """
  calculate the annualized yield_to_maturity on a bond
  """
  upper = 1
  lower = 0
  while True:
    test_rate = (upper + lower)/2
    guess = bond_price(fv, c, n, m, test_rate)
    error = guess - price
    if abs(error) < accuracy:
      break
    if guess > price:
      lower = test_rate
    else:
      upper = test_rate
  return test_rate

if __name__ == '__main__':

    times = cashflow_times(5,2)
    cashflows = bond_cashflows(100,0.04,5,2)
    df = discount_factors(0.02, 5, 2)
    price = bond_price(100, 0.04, 3, 2, 0.03)
    ytm = bond_yield_to_maturity(1000, 0.08, 5, 1, 950)

