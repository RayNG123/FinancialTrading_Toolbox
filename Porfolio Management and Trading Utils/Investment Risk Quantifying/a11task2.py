#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 11
#File Description: This file contains a set of functions to process a series of 
#stock prices returns and compute drawdown accordingly. One function of the function
#is able to plot visualize the tend for drawdown. And another one could conduct a 
#monte carlo simulation and compute drawdown percentage accordingly
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from a9task1 import MCStockSimulator

def compute_drawdown(prices):
    """
    processes a column of asset prices and computer drawdown as a number and
    percentage
    """
    #Check for data type and assign value and index accordindlu
    if isinstance(prices,(pd.DataFrame,pd.Series)):
      index = prices.index
      values = prices.values.squeeze()
    elif isinstance(prices,np.ndarray):
      values = prices.squeeze()
      index = list(range(values.shape[0]))
    else:
      raise AttributeError('Data Type not Accepted')

    #calculate cumulative max, drawdown in dollars and percentage
    prev_max = np.maximum.accumulate(values)
    dd_dollars = prev_max - values
    dd_pct = dd_dollars/prev_max

    #store result as a pandas dataframe with date as an index
    result = pd.DataFrame({'Date':index, 
                           'prices':values,
                           'prev_max':prev_max,
                           'dd_dollars':dd_dollars,
                           'dd_pct':dd_pct})
    return result.set_index('Date',drop = True)  


def plot_drawdown(df):
    """
    create and show two charts:
    1 - The historical price and previous maximum price.
    2 - The drawdown since previous maximum price as a percentage lost
    """
    # check for data type and extract data needed
    assert isinstance(df, pd.DataFrame), 'Only DataFrame Accepted'
    prices = df['prices']
    index = df.index
    prev_max = df['prev_max']
    dd_pct = df['dd_pct']
    
    #plot price trend and cummulative max price trend
    plt.plot(index,prices,label = 'price')
    plt.plot(index,prev_max,label = 'prev_max')
    plt.xticks(rotation = 45)
    plt.xlabel('Date')
    plt.title('Price and Previous Maximum')
    plt.legend()
    plt.show()
    
    #clear graph and plot drawdown percentage
    plt.clf()
    plt.plot(index,dd_pct,label = 'dd_pct')
    plt.xticks(rotation = 45)
    plt.xlabel('Date')
    plt.title('Drawdown Percentage')
    plt.legend()
    plt.show()

def run_mc_drawdown_trials(init_price,  years, r, sigma, trial_size, num_trials):
    """
    use the Monte Carlo stock simulation that you wrote in Assignment 8 to 
    simulate the price path evoluation of a stock
    """
    result = []
    
    #Iterate over total number of trials
    for i in range(num_trials):
        
      #initiate a simulator to create a series of return
      #maximum draw are then calculated and stored
      stimulator = MCStockSimulator(init_price, years, r, sigma, trial_size)
      prices = stimulator.generate_simulated_stock_values()
      report = compute_drawdown(prices)['dd_pct']
      result.append(report.max())
    return pd.Series(result)