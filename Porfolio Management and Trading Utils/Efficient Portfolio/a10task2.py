#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 9
#File Description: This file contains a set of functions cooperating with numpy pacakge
#matrix operation to effciently compute stock portfolio opertion and related statistics,
#including portfolio return, standard deviation, global minimum variance portfolio, efficient
#portfolio standard deviation under a certain rate, and sets of function to process stock
#price csv file to getc returns and covariance matrix

from a10task1 import *
import numpy as np
import pandas as pd

def calc_portfolio_return(e, w):
    """
    calculates and returns the portfolio return (as a float)
    for a portfolio of n >= 2 assets
    """
    return (e*w.T).item()

def calc_portfolio_stdev(v, w):
    """
    calculates and returns the portfolio standard deviation (as 
    a float) for a portfolio of n >= 2 assets
    """
    return np.sqrt((w*v*w.T).item())

def calc_global_min_variance_portfolio(v):
    """
    returns the portfolio weights corresponding to the global 
    minimum variance portfolio
    """
    c = np.ones((1,v.shape[0]))*v.I*np.ones((v.shape[1],1))
    sigma = 1/c
    return sigma*np.ones((1,v.shape[0]))*v.I

def calc_min_variance_portfolio(e, v, r):
    """
    finds and returns the portfolio weights corresponding to the 
    minimum variance portfolio for the required rate of return r
    """
    #compute related parameters a, b, c
    a = (np.ones((1,v.shape[0]))*v.I*e.T).item()
    b = (e*v.I*e.T).item()
    c = (np.ones((1,v.shape[0]))*v.I*np.ones((v.shape[1],1))).item()
    
    #get realted matrix parameter and determinant
    A = np.matrix([[b,a],[a,c]])
    d = np.linalg.det(A)

    #compute final portfolio variance
    g = (1/d)*(b*np.ones((1,v.shape[0])) - a*e)*v.I
    h = (1/d)*(c*e - a*np.ones((1,v.shape[0])))*v.I
    return g + h*r

def calc_efficient_portfolios_stdev(e, v, rs):
    """
    finds a series of minimum variance portfolios and returns 
    their standard deviations
    """
    result = []
    
    #Iterate over each rate to get stdevs
    for r in rs:
      weight = calc_min_variance_portfolio(e, v, r)
      sigma = calc_portfolio_stdev(v, weight)
      
      #print out each stdev and related metrics
      string = np.array2string(weight,formatter={'float_kind': '{:>11.8f}'.format}, prefix='', suffix='')
      print(f'r = {r:.4f}, sigma = {sigma:.4f}  w = {string}')
      result.append(sigma)
    return np.array(result)

def get_stock_prices_from_csv_files(symbols):
    """
    obtain a pandas.DataFrame containing historical stock 
    prices for several stocks
    """
    #Iterate over each sotck files
    for i,symbol in enumerate(symbols):
      fn = f"./{symbol}.csv"
      
      #create a DataFrame with first stock price and date
      if i == 0:
        data = pd.read_csv(fn)
        length = data.shape[0]
        Date = data['Date']
        result = pd.DataFrame({'Date':Date, symbol:data['Adj Close']})
     
    #Check if length euqal and append other stock prices
      else:
        data = pd.read_csv(fn)
        assert data.shape[0] == length, "Input files has different length"
        result[symbol] = data['Adj Close']
    return result
        
def get_stock_returns_from_csv_files(symbols):
    """
    return a single pandas.DataFrame object containing the 
    stock returns
    """
    prices = get_stock_prices_from_csv_files(symbols)
    
    #Iterate over all stocks to get return rate
    for symbol in symbols:
      prices[symbol] = prices[symbol].pct_change()
    return prices

def get_covariance_matrix(returns):
    """
    generates a covariance matrix for the stock returns in returns
    """
    return returns.cov()




