#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 10
#File Description: This file contains three functions foc stock price and return
#risk estimation. Two way of calculating value at risk for a stock return series
#is included

def compute_model_var_pct(mu, sigma, x, n):
    """
    compute the value at risk as a percentage of the asset/portfolio 
    value, assumin a normal distribution
    """
    return mu*n + norm.ppf(1 - x)*sigma*n**(1/2)

def get_historical_returns(filename):
    """
    read historical stock price adjusted returns are retrurn it as
    a pandas series
    """
    #read data and check type
    data = pd.read_csv(filename)
    assert 'Adj Close' in data.columns, "Target column not detected"
    
    #select adjusted close price column
    data.set_index('Date',inplace = True)
    return data['Adj Close'].pct_change().dropna()

def compute_historical_var_pct(returns, x, n):
    """
    compute the VaR (as a percentage) using the historical simulation 
    approach
    """
    #get histocial return statistics
    returns = returns.rename('r')
    print(returns.describe())

    #Get value at risk
    print('\t')
    var = returns.quantile(1 - x)*n**(1/2)
    print(f'With the compute_historical_var_pct estimate, we are {x}% confident that the maximum loss over {n} days would not exceed {var:.2%}')
    return var