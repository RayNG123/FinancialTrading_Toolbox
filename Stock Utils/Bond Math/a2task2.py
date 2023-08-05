#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:13:50 2023
name: Yusen Wu
Email: wuyusen@bu.edu
Assigment: 1
"""

from a2task1 import *

def bond_duration(fv, c, n, m, r):
  """
  calculate and return the duration metric for a bond
  """
  B_0 = bond_price(fv, c, n, m, r)
  cashflows = bond_cashflows(fv, c, n, m)
  discount = discount_factors(r, n, m)
  times = cashflow_times(n, m)
  return sum([times[i]*cashflows[i]*discount[i] for i in range(len(cashflows))])/(B_0*m)

def macaulay_duration(fv, c, n, m, price):
  """
  to calculate and return the Macaulay duration for a bond.
  """
  ytm = bond_yield_to_maturity(fv, c, n, m, price)
  B_0 = bond_price(fv, c, n, m, ytm)
  cashflows = bond_cashflows(fv, c, n, m)
  times = cashflow_times(n, m)
  
  return sum([times[i]*cashflows[i]/((1 + ytm/m)**times[i]) for i in range(len(cashflows))])/(B_0*m)

def modified_duration(fv, c, n, m, price): 
  """
  calculate and return the Macaulay duration for a bond
  """
  dmac = macaulay_duration(fv, c, n, m, price)
  ytm = bond_yield_to_maturity(fv, c, n, m, price)
  return dmac/(1 + ytm/m)

def bond_convexity(fv, c, n, m, r):
  """
  calculate and return the Macaulay duration for a bond
  """
  B_0 = bond_price(fv, c, n, m, r)
  cashflows = bond_cashflows(fv, c, n, m)
  discount = discount_factors(r, n, m)
  times = cashflow_times(n, m)
  return sum([times[i]*cashflows[i]*discount[i]*(times[i] + 1) for i in range(len(cashflows))])/((B_0*m**2)*(1 + r/m)**2)

def estimate_change_in_price1(fv, c, n, m, price, dr):
  """
  return the estimated dollar change in price corresponding to a change in yield
  """
  return - modified_duration(fv, c, n, m, price)*dr*price

def estimate_change_in_price2(fv, c, n, m, price, dr):
  """
  return the estimated dollar change in price corresponding to a change in yield
  """
  ytm = bond_yield_to_maturity(fv, c, n, m, price)
  return (-modified_duration(fv, c, n, m, price)*dr + 1/2*bond_convexity(fv, c, n, m, ytm)*(dr**2))*price

if __name__ == '__main__':

    bond_duration(1000, 0.08, 5, 2, 0.07)
    macaulay_duration(1000, 0.08, 5, 2, 950)
    modified_duration(1000, 0.08, 5, 2, 950)
    bond_convexity(5000, 0.05, 3, 2, 0.05)
    estimate_change_in_price1(1000, 0.07, 5, 2, 1000, 0.0001)
    estimate_change_in_price2(1000, 0.07, 5, 2, 1000, -0.01)
