#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 12
#File Description: This file contains a set of functions to process a series of 
#stock prices returns and implemented a trading strategy to decide buy and sell
#according to cross bewteen stock price and related statistics(Comparasion bewteen 
#2 rolling mean. Backtesting is asoimplemented, visualization for cumulative returns 
#is available

import pandas as pd
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

def create_double_moving_average(df, window1 = 5, window2 = 30, column_name = None):
    """
    create different rollingmean with different periods according to user specified
    number of periods
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

    #Caculate all related rolling mean with different periods
    result['RollingMeanShort'] = result['Observations'].rolling(window = window1).mean()
    result['RollingMeanLong'] = result['Observations'].rolling(window = window2).mean()
    return result

def create_long_short_position_moving_average(df,trading_fee = True):
    """
    create the position to signal buy or sell signal accodinging to the cross
    between moving averages with different periods
    """
    #Creat a dataframe to hold output result
    position = pd.DataFrame(index=df.index, columns=['Position'])
    position['Position'] = None
    if trading_fee:
      position['Trading'] = 0

    #Iterate over each day to check if there is a buy or sell signal
    for i in range(len(df)-1):
        #if short term rolling mean is larger than long term rolling mean, buy
        if df['RollingMeanShort'][i] > df['RollingMeanLong'][i]:
            position['Position'][i+1] = 1

        #if short term rolling mean is smaller than long term rolling mean, sell
        elif df['RollingMeanShort'][i] < df['RollingMeanLong'][i]:
            position['Position'][i+1] = 0

        #if no signal, position stays the same as the previous day
        else:
            position['Position'][i+1] = position['Position'][i]

        #add trading fee positions if specified
        if trading_fee and position['Position'][i+1] != position['Position'][i]:
            position['Trading'][i+1] = 1
    return position

def calculate_long_short_returns_moving_average(df, position, trading_fee = True, column_name = None):
    """
    calculate market, strategy, and abnormal return accoding to the stock and
    your speficied training strategy
    """
    #create statistic needed to calculate signal
    data = create_double_moving_average(df, column_name = column_name)

    #create a dataframe to hold output market, strategy, and abnormal returns
    result = pd.DataFrame(index = data.index)
    result['Market Return'] = data['Observations'].pct_change()

    #add trading fee if specified
    if trading_fee:
      result['Trading_Fee'] = abs(position['Trading']*result['Market Return'])*(-0.0025)
      result['Strategy Return'] = result['Market Return']*position['Position'] + result['Trading_Fee']
      result = result.drop('Trading_Fee', axis = 1)
    else: 
      result['Strategy Return'] = result['Market Return']*position['Position']
    result['Abnormal Return'] = result['Strategy Return'] - result['Market Return']
    return result

def plot_cumulative_returns(df):
    """
    Generate a plot for the cumulative return of market, startegy, and abnormal returns
    """
    df.cumsum().plot()
    plt.title('Cumulative Returns')