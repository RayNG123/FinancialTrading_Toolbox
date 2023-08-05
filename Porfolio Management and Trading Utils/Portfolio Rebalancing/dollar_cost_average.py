#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 13
#File Description: This file contains a set of functions to implement a dolloar cost
# average algorithm and a function to visualize the result. The file also contains a 
#portfolio algorithm that can assign weight to indicidual stock without rebalancing or 
#with reblancing. A function is implemented to help plot stock relative weight over time

import pandas as pd
import math
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

def dollar_cost_average(prices, total_inv=10000, num_purchases=12):
    """
    implement a dollar-cost averaging strategy that will divide investment 
    evenly to different period and check the result
    """
    #get the investment interval and payment
    time = math.ceil(len(prices)/num_purchases)
    payment = total_inv/num_purchases
    result = pd.DataFrame({'prices':prices}, index = prices.index)

    #create a dataframe to hold result
    result['shares'] = 0
    result['cash_value'] = total_inv
    result['stock_value'] = 0

    #interate over each day to caluclate daily price and return
    for idx in range(len(result)):

      #for the first buy period
      if idx % time == 0:
        if idx == 0:
          #buy stocks, increas stock value and decrease cash calue
          result['shares'][idx] = payment/result['prices'][idx]
          result['stock_value'][idx] = payment
          result['cash_value'][idx] -= payment

        #for other buy period
        else:
          #buy stocks, increas stock value and decrease cash calue
          result['shares'][idx] = payment/result['prices'][idx] + result['shares'][idx-1]
          result['stock_value'][idx] = result['shares'][idx]*result['prices'][idx]
          result['cash_value'][idx] = result['cash_value'][idx-1] - payment

      #for non buy period
      else:
        #chas value do not change, stock value follow market
        result['shares'][idx] = result['shares'][idx-1]
        result['stock_value'][idx] = result['shares'][idx]*result['prices'][idx]
        result['cash_value'][idx] = result['cash_value'][idx-1]

    #get final portfolio value
    result['portfolio'] = result['stock_value'] + result['cash_value']
    return result

def compare_returns(df):
    """
    given the market and portfolio value, calculate and display 
    the periodic market return, strategy return, and abnormal returns
    """
    #read data and display last 5 rows
    result = df[['market','portfolio']]
    print('Showing the last several rows of data (values):')
    print(result.tail(5))
    print('\t')

    #get market, strategy, and abnormal return
    returns = result.pct_change()
    returns.columns = ['mkt_ret','str_ret']
    returns['abn_ret'] = returns['str_ret'] - returns['mkt_ret']
    print('Descriptive Statistics for Returns:')

    #Print related statistics
    print(returns.describe())
    print('\t')

    #draw return plot
    result.plot()
    plt.title('Portfolio Values')

    #draw cumulative return plot
    returns.cumsum().plot()
    plt.title('Cumulative Returns')
    return returns

def create_target_weight_portfolio(prices, target_weights, initial_value = 10000):
    """
    return a DataFrame with columns containing the values (standardized to 
    $10,000 or the initial_value) of an target-weighted investment in each 
    of the assets in prices, as well as the value of the total portfolio, 
    without ever rebalancing.
    """
    #get the price and return for each stock
    result = prices[target_weights.keys()]
    returns = result.pct_change()
    result['portfolio'] = 0

    #iterate over each day to get stock prices
    for idx in range(len(result)):

      #for the first rebalance period
      if idx == 0:

        #each stock equal to initial value times weight
        for i in target_weights.keys():
          result[i][idx] = target_weights[i]*initial_value
          result['portfolio'][idx] = initial_value
      else:

        #for other days stock value follows the market
        for i in target_weights.keys():
          result[i][idx] = result[i][idx-1]*(1 + returns[i][idx])
          result['portfolio'][idx] += result[i][idx]
    return result

def plot_relative_weights_over_time(values):
    """
    plot the relative weights of assers in the portfolio, standardized to 1
    """
    weights = values.drop(columns=['portfolio'])

    #iterate over each stock and set weight
    for i in weights.columns:
      weights[i] = weights[i]/values['portfolio']

    #plot relative weight
    weights.plot()
    plt.title('Portfolio Weights')


def create_rebalanced_portfolio(prices, target_weights, rebalance_freq, initial_value = 10000):
    """
    implement a portfolio rebalancing algorithm, that will assign each portfolio the weight
    of initial value, and adjust to the same weight according to specified rebalance frequency
    """
    #get the price and return for each stock
    result = prices[target_weights.keys()]
    returns = result.pct_change()
    result['portfolio'] = 0

    #Iterate over each day to get stock price and rebalance if needed
    for idx in range(len(result)):

      #for the each rebalance period
      if idx%rebalance_freq == 0:

        #for the first rebalance period
        if idx == 0:
          #each stock equal to initial value times weight
          #portfolio value is sum of individual stock
          for i in target_weights.keys():
            result[i][idx] = target_weights[i]*initial_value
            result['portfolio'][idx] = initial_value

        #for the other rebalance period
        else:
            #get the returns for individual stock and portfolio at that day
            for i in target_weights.keys():
              result[i][idx] = result[i][idx-1]*(1 + returns[i][idx])
              result['portfolio'][idx] += result[i][idx]

            #then rebalance
            for i in target_weights.keys():
              result[i][idx] = result['portfolio'][idx]*target_weights[i]
      
      #for other days, stock price follows the market
      else:
        for i in target_weights.keys():
          result[i][idx] = result[i][idx-1]*(1 + returns[i][idx])
          result['portfolio'][idx] += result[i][idx]
    return result