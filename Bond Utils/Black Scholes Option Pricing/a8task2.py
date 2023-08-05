#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 8
#File Description: This file contains a set of user defined class to build a option pricing
#table and calculate the implied volatility under a specific price of the option

from a8task1 import *

def generate_option_value_table(s, x, t, sigma, rf, div):
    """
    generate a printout to illustrate the change in option prices with r
    espect to the change in the underlying stock price
    """
    #Initialize call and put option for testing
    call = BSMEuroCallOption(s, x, t, sigma, rf, div)
    put = BSMEuroPutOption(s, x, t, sigma, rf, div)
    
    #print out the headlines
    print(call)
    print(put)
    print('\n')
    
    #Iterate over each possible price to print put undelaying call and put value
    print('Change in option values w.r.t. change in stock price:')
    print('  price        call value        put value        call delta        put delta')
    for price in range(s - 10, s + 11):
      call.s = price
      put.s = price
      print(f'${call.s:>7.2f}{call.value():>15.4f}{put.value():>18.4f}{call.delta():>17.4f}{put.delta():>18.4f}')

def calculate_implied_volatility(option, value, accuracy = 0.001):
    """
    calculate the implied volatility of an observed option
    """
    assert isinstance(option, BSMOption)
    upper = 1
    lower = 0
    
    #a bisection algorithm to find suitable value
    while True:
      test_rate = (upper + lower)/2
      option.sigma = test_rate
      test_value = option.value()
      
      #if test value is accurate then return
      if abs(test_value - value) <= accuracy:
        return test_rate
    
      #else adjust the searching range
      else:
        if test_value > value:
          upper = test_rate
        else:
          lower = test_rate