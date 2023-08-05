#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 7
#File Description: This file contains a set of functions to build a euro call
#and put value tree, and a amer put value tree

from a7task1 import *

def build_euro_call_value_tree(s, x, sigma, rf, div, T, n):
    """
    builds and returns a binomial option value tree for European-style call options
    """
    #build the price tree and the up-down probability associated
    p = get_risk_neutral_probability(sigma, rf, div, T/n)
    price_tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)

    #set the price of tree nodes at the end
    for i in range(len(price_tree)):
      price_tree[i][-1] = max(price_tree[i][-1]-x, 0)

    #set the price of each tree node recursively back to front to get PV
    for j in range(len(price_tree[0])-2,-1,-1):
      for i in range(len(price_tree)-2,-1,-1):
        #only change price on above diagonal
        if j >= i:
          price_tree[i][j] = math.exp(-rf*(T/n))*(p*price_tree[i][j+1] + (1 - p)*price_tree[i+1][j+1])

    return price_tree
      
def euro_call_value(s, x, sigma, rf, div, T, n):
    """
    calculates and returns the current value for European-style call option
    """
    return build_euro_call_value_tree(s, x, sigma, rf, div, T, n)[0][0]

def build_euro_put_value_tree(s, x, sigma, rf, div, T, n):
    """
    builds and returns a binomial option value tree for European-style put options
    """
    #build the price tree and the up-down probability associated
    p = get_risk_neutral_probability(sigma, rf, div, T/n)
    price_tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)

    #set the price of tree nodes at the end
    for i in range(len(price_tree)):
        price_tree[i][-1] = max(x - price_tree[i][-1], 0)

    #set the price of each tree node recursively back to front to get PV
    for j in range(len(price_tree[0])-2,-1,-1):
      for i in range(len(price_tree)-2,-1,-1):
        #only change price on above diagonal
        if j >= i:
          price_tree[i][j] = math.exp(-rf*(T/n))*(p*price_tree[i][j+1] + (1 - p)*price_tree[i+1][j+1])

    return price_tree

def euro_put_value(s, x, sigma, rf, div, T, n):
    """
    calculates and returns the current value for European-style put option
    """
    return build_euro_put_value_tree(s, x, sigma, rf, div, T, n)[0][0]

def build_amer_put_value_tree(s, x, sigma, rf, div, T, n):
    """
    builds and returns a binomial option value tree for American-style put options
    """
    #build the price tree and the up-down probability associated
    #a stock tree is copied to record stock price in each tree node
    p = get_risk_neutral_probability(sigma, rf, div, T/n)
    price_tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)
    stock_tree = [[i for i in j] for j in price_tree]

    #set the price of tree nodes at the end
    for i in range(len(price_tree)):
      price_tree[i][-1] = max(x - price_tree[i][-1], 0)

    #set the price of each tree node recursively back to front to get PV
    for j in range(len(price_tree[0])-2,-1,-1):
      for i in range(len(price_tree)-2,-1,-1):
        #only change price on above diagonal
        if j >= i:
          price_A = math.exp(-rf*(T/n))*(p*price_tree[i][j+1] + (1 - p)*price_tree[i+1][j+1])
          price_B = x - stock_tree[i][j]
          price_tree[i][j] = max(price_A, price_B)

    return price_tree

def amer_put_value(s, x, sigma, rf, div, T, n):
    """
    calculates and returns the current value for American-style put option
    """
    return build_amer_put_value_tree(s, x, sigma, rf, div, T, n)[0][0]