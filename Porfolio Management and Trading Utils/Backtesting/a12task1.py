#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 12
#File Description: This file contains a set of functions to process a series of 
#stock prices returns and implemented a trading strategy to decide buy and sell
#according to cross bewteen stock price and related statistics. Backtesting is aso
#implemented, visualization for cumulative returns is available

import pandas as pd
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

def create_bollinger_bands(df, window = 21, no_of_std = 1, column_name = None):
    """
    create Bollinger bands with rolling mean and standard deviation given 
    a set of stock prices
    """
    #Check if column provided and select the corresponding one
    if column_name == None:
      #check if left most column the date
      if df.columns[0] == 'Date':
        target = df[df.columns[1]]
      else:
        target = df[df.columns[0]]

    #Set target the column specified by users
    else:
      assert column_name in df.columns, 'Target Column not Detected in df'
      target = df[column_name]

    #Creat a dataframe to hold output result
    result = pd.DataFrame(index = df.index)
    result['Observations'] = target

    #Caculate all related statistics like rolling mean, upper bound and lower bound
    result['RollingMean'] = result['Observations'].rolling(window = window).mean()
    result['RollingStd'] = result['Observations'].rolling(window = window).std()
    result['UpperBound'] = result['RollingMean'] + no_of_std*result['RollingStd']
    result['LowerBound'] = result['RollingMean'] - no_of_std*result['RollingStd']
    return result.drop(columns = ['RollingStd'])

def create_long_short_position(df):
    """
    create the position to signal buy or sell signal accodinging to the cross
    between stock price and its lower and upper bound
    """
    #Creat a dataframe to hold output result
    position = pd.DataFrame(index=df.index, columns=['Position'])
    position['Position'] = None

    #Iterate over each day to check if there is a buy or sell signal
    for i in range(len(df)-1):
        if df['Observations'][i] > df['UpperBound'][i]:
            position['Position'][i+1] = 1
        elif df['Observations'][i] < df['LowerBound'][i]:
            position['Position'][i+1] = -1

        #if no signal, position stays the same as the previous day
        else:
            position['Position'][i+1] = position['Position'][i]
    return position

def calculate_long_short_returns(df, position, column_name = ''):
    """
    calculate market, strategy, and abnormal return accoding to the stock and
    your speficied training strategy
    """
    #create statistic needed to calculate signal
    data = create_bollinger_bands(df, column_name = column_name)

    #create a dataframe to hold output market, strategy, and abnormal returns
    result = pd.DataFrame(index = data.index)
    result['Market Return'] = data['Observations'].pct_change()
    result['Strategy Return'] = result['Market Return']*position['Position']
    result['Abnormal Return'] = result['Strategy Return'] - result['Market Return']
    return result

def plot_cumulative_returns(df):
    """
    Generate a plot for the cumulative return of market, startegy, and abnormal returns
    """
    df.cumsum().plot()
    plt.title('Cumulative Returns')