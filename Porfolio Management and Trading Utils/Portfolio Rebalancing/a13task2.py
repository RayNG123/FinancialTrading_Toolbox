#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 13
#File Description: This file contains a experiment to compare portfolio value 
#under different seeting, for exmaple, rebalance or not and using efficient 
#portfolio weight or not. Statistic and graph will be produced to show the 
#output result, including portfolio weight, returns, and cumulative returns
#Need stock file to execute the program

from a10task1 import *
from a10task2 import *
from a11task1 import *
from a11task2 import *
from a13task1 import *

#if want to do experiment, change False to True and read stock file
if False:
    stocklist = ['AAPL.csv','GOOG.csv','AMZN.csv','BIDU.csv','BABA.csv']
    stockdata = {i[:-4]:pd.read_csv(i).set_index('Date')['Adj Close'] for i in stocklist}

def implement_and_visualize_strategy(stocklist, 
                                     stockdata,  
                                     equal_weight = True, 
                                     initial_value = 10000,
                                     rebalance = True,
                                     rebalance_freq = 20,
                                     start_of_train = '2014-12-01',
                                     start_of_test = '2019-12-01',
                                     end_of_test = '2020-12-01'):
    """
    implemented rebalance and efficient portfolio algorithm accoding to specification
    """
    #divide stock data into train and test data
    train_data = [stockdata[i].loc[start_of_train:start_of_test].pct_change()[1:].tolist() for i in stockdata.keys()]
    test_data = [stockdata[i].loc[start_of_test: end_of_test] for i in stockdata.keys()]

    if not equal_weight:
      #implement efficient frontier algorithm and gte expecetd return and covariance
      expected_return = np.matrix(train_data).mean(axis = 1).squeeze()
      cov = np.matrix(np.cov(np.matrix(train_data)))

      #get desired return rate
      N = expected_return.shape[1]
      weights = np.ones(N) / N 
      expected_portfolio_return = float(expected_return@weights)
  
      #get weight for global least variance portfolio
      weights = calc_min_variance_portfolio(expected_return,cov,expected_portfolio_return)
      target_weights = {i[:-4]:j for i,j in zip(stocklist,weights.tolist()[0])}
    else: 
      #equal weight
      target_weights = {i[:-4]:1/len(stocklist) for i in stocklist}

    #get test stock prices
    prices = {i[:-4]:j for i,j in zip(stocklist,test_data)}
    prices = pd.DataFrame(prices)

    #implement rebalance
    if rebalance:
      values  = create_rebalanced_portfolio(prices, 
                                            target_weights, 
                                            rebalance_freq = rebalance_freq, 
                                            initial_value = initial_value)
      
    #no rebalance
    else:
      values = create_target_weight_portfolio(prices, 
                                              target_weights, 
                                              initial_value = initial_value)

    #plot relative weight
    plot_relative_weights_over_time(values)

    #show statistics
    returns = values / values.shift(1) - 1
    print('Related Statistics for Efficeint Weight and Rebalance each 20 Days')
    print(returns.describe())

    #show 10 day 2% value at risk and maximum drawdown
    a = compute_historical_var_pct(returns['portfolio'], 0.98, 10)
    print()
    drawdown = compute_drawdown(values['portfolio'])
    max_idx = drawdown['dd_dollars'].idxmax()
    print('The Maximum Drawdown is:')
    print(drawdown.loc[max_idx,])


    #plot returns
    returns.plot()
    plt.title('Individual Stock and Portfolio Returns for Efficeint Weight and Rebalance each 20 Days')
    plt.show()

    #plot cumulative returns
    returns.cumsum().plot()
    plt.title('Cumulative Individual Stock and Portfolio Returns for Efficeint Weight and Rebalance each 20 Days')
    plt.show()

#Change False to True if want to do experiment
if False:
    #euqal and no rebalance
    implement_and_visualize_strategy(stocklist, 
                                    stockdata,  
                                    equal_weight = True, 
                                    initial_value = 10000,
                                    rebalance = False,
                                    rebalance_freq = 20,
                                    start_of_train = '2014-12-01',
                                    start_of_test = '2019-12-01',
                                    end_of_test = '2020-12-01')
    
    #euqal and rebalance
    implement_and_visualize_strategy(stocklist, 
                                    stockdata,  
                                    equal_weight = True, 
                                    initial_value = 10000,
                                    rebalance = True,
                                    rebalance_freq = 20,
                                    start_of_train = '2014-12-01',
                                    start_of_test = '2019-12-01',
                                    end_of_test = '2020-12-01')
    
    #efficient and no rebalance
    implement_and_visualize_strategy(stocklist, 
                                    stockdata,  
                                    equal_weight = False, 
                                    initial_value = 10000,
                                    rebalance = False,
                                    rebalance_freq = 20,
                                    start_of_train = '2014-12-01',
                                    start_of_test = '2019-12-01',
                                    end_of_test = '2020-12-01')
    
    #efficient and rebalance
    implement_and_visualize_strategy(stocklist, 
                                    stockdata,  
                                    equal_weight = False, 
                                    initial_value = 10000,
                                    rebalance = True,
                                    rebalance_freq = 20,
                                    start_of_train = '2014-12-01',
                                    start_of_test = '2019-12-01',
                                    end_of_test = '2020-12-01')