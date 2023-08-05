#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 9
#File Description: This file contains three functions foc stock price and return
#visualization including stock price chart, cumulative change chart, and efficient
#frontier chart

from a10task2 import *
import matplotlib.pyplot as plt

def plot_stock_prices(symbols): 
    """
    which creates a graph of the historical stock prices for 
    several stocks
    """
    #Get prices from csv file
    prices = get_stock_prices_from_csv_files(symbols)
    
    #Plot price for all stock prices and date
    prices['Date'] = pd.to_datetime(prices['Date'])
    prices.plot(x='Date', y = symbols)
    
    #Specify ylable and title
    plt.ylabel('Price')
    plt.title('stock prices')

def plot_stock_cumulative_change(symbols):
    """
    creates a graph of the cumulative stock returns for several stock
    """
    #Get returns for each stock
    prices = get_stock_returns_from_csv_files(symbols).set_index('Date')
    
    #Get cummulative change 
    prices.iloc[0,] = 1
    prices = prices.cumsum()
    prices.reset_index(inplace = True)
    
    #Plot cumulative change and date
    prices['Date'] = pd.to_datetime(prices['Date'])
    prices.plot(x='Date', y = symbols)
    
    #Specify ylable and title
    plt.ylabel('Relative Price')
    plt.title('cumulative change in stock prices')

def plot_efficient_frontier(symbols):
    """
    to create a graph of the efficient frontier (the set of minimum 
    variance portfolios) that can be achieved using a small set of assets.
    """
    #Get returns and covariance matrix
    returns = get_stock_returns_from_csv_files(symbols)
    cov = np.matrix(get_covariance_matrix(returns))
    
    #Find  global minimum variance point
    avg_return = np.matrix(np.array(returns.mean()))
    min_weights = calc_global_min_variance_portfolio(cov)
    min_rs = calc_portfolio_return(avg_return, min_weights)
    
    #get a set of possible rates and related stdevs
    rs = np.linspace(min_rs-0.10, min_rs + 0.10)
    stdevs = calc_efficient_portfolios_stdev(avg_return, cov, rs)
    return_rate = []
    
    #Iterate over each rate to get expected returns
    for r in rs:
      weights = calc_min_variance_portfolio(avg_return, cov, r)
      return_rate.append(calc_portfolio_return(avg_return, weights))
    
    #plot the efficient frontier
    plt.plot(stdevs,return_rate)
    
    #Specify all labels and title
    plt.xlabel('Portfolio Standard Deviation')
    plt.ylabel('Portfolio Expected Return')
    plt.title('Efficient Frontier')
    plt.show()