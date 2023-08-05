#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Yusen Wu 
Email Address: wuyusen@bu.edu 
Assignment: 3
File Description: 
    This task includes several functions several functions to calculate returns
    for a list of stock prices, read and store a list of stocks prices from a csv file,
    generate and print a report for multiple stocks
"""

from a3task1 import *

def calc_returns(prices):
  """
  This function will process a list of stock prices and calculate 
  the periodic returns
  """
  returns = []
  #Loop over each adjacent pair of prices to get all return rates
  for i in range(len(prices)-1):
    returns.append(prices[i+1]/prices[i]-1)
  return returns

def process_stock_prices_csv(filename):
  """
  process a data file containing stock price data, and return 
  a list of stock prices.
  """
  with open(filename, 'r') as file:
    data = file.readlines()
  price = []
  #ignore headers and loop over all remaining lines to get the adj close price of each day
  for i in data[1:]:
    price.append(float(i.strip().split(',')[-2]))
  return price

def stock_report(filenames):
  """
  a client program to process stock prices and display 
  (print out) descriptive statistics about the stocks. 
  """
  data = []

  #Loop over all filenames and store results as [filename, prices]
  for filename in filenames:
    data.append([filename[:-4], process_stock_prices_csv(filename)])

  #Loop over all stocks and store results as [filename, returnss]
  for stock in data:
    stock[1] = calc_returns(stock[1])

  #Print out symbols, means, stdevs of all stocks
  symbols = ''.join([f'{i[0]:>12}' for i in data])
  print(f'Symbol:{symbols}')

  means = ''.join([f'{mean(i[1]):>12.5f}' for i in data])
  print(f'Mean:  {means}')

  stdevs = ''.join([f'{stdev(i[1]):>12.5f}' for i in data])
  print(f'StDev: {stdevs}')

  #if their is a market index to compare, print out corraviances, correlations, rsqs, alphas, betas of all stocks
  market_returns = data[-1][1]

  covars = ''.join([f'{covariance(i[1],market_returns):>12.5f}' for i in data])
  print(f'Covar: {covars}')
  
  correls = ''.join([f'{correlation(i[1],market_returns):>12.5f}' for i in data])
  print(f'Correl:{correls}')

  rsqs = ''.join([f'{rsq(i[1],market_returns):>12.5f}' for i in data])
  print(f'R-SQ:  {rsqs}')

  betas = ''.join([f'{simple_regression(market_returns,i[1])[1]:>12.5f}' for i in data])
  print(f'Beta:  {betas}')

  alphas = ''.join([f'{simple_regression(market_returns,i[1])[0]:>12.5f}' for i in data])
  print(f'Alpha: {alphas}')