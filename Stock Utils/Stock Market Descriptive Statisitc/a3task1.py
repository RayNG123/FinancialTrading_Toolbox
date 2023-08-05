#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Yusen Wu 
Email Address: wuyusen@bu.edu 
Assignment: 3
File Description: 
    This task includes several functions to process a list of numbers and 
    generate the following descriptive statistics: mean, variance, standard deviation, 
    covariance, correlation, and, simple regression. 
"""

def mean(values):
  """
  takes as a parameter a list of numbers, and 
  calculates and returns the mean of those values
  """
  return sum(values)/len(values)

def variance(values):
  """
  takes as a parameter a list of numbers, and calculates 
  and returns the population variance of the values in that list
  """
  diffs = [(value - mean(values))**2 for value in values]
  return sum(diffs)/len(diffs)

def stdev(values):
  """
  takes as a parameter a list of numbers, and calculates 
  and returns the population standard deviation of the 
  values in that list
  """
  return variance(values)**0.5

def covariance(x,y):
  """
  takes as parameters two lists of values, and calculates 
  and returns the population covariance for those two lists
  """
  #value_x to record each x's diffs bewteen their mean
  value_x = [value - mean(x) for value in x]

  #value_y to record each y's diffs bewteen their mean
  value_y = [value - mean(y) for value in y]

  #value_x_y to record product of each corresbonding value in value_x and value_y
  value_x_y = [value_x[i]*value_y[i] for i in range(len(x))]
  return sum(value_x_y)/len(value_x_y)

def correlation(x,y):
  """
  takes as parameters two lists of values, and calculates 
  and returns the correlation coefficient between these 
  data series
  """
  return covariance(x,y)/(stdev(x)*stdev(y))

def rsq(x,y):
  """
  that takes as parameters two lists of values, and calculates 
  and returns the square of the correlation between those two 
  data series
  """
  return correlation(x,y)**2

def simple_regression(x,y):
  """
  that takes as parameters two lists of values, and calculates 
  and returns the regression coefficients between these data series. 
  The function should return a list containing two values: the 
  intercept and regression coefficients, α and β.
  """
  beta = covariance(x,y)/variance(x)
  alpha = mean(y) - beta*mean(x)
  return alpha, beta

if __name__ == '__main__':
    # test the functions:
    print('mean([4,4,3,6,7]):', mean([4,4,3,6,7]))
    print('variance([[4,4,3,6,7]):', variance([4,4,3,6,7]))
    print('stdev([4,4,3,6,7]):', stdev([4,4,3,6,7]))
    print('covariance([4,4,3,6,7], [6,7,5,10,12]):', covariance([4,4,3,6,7], [6,7,5,10,12])) 
    print('correlation([4,4,3,6,7], [6,7,5,10,12]):', correlation([4,4,3,6,7], [6,7,5,10,12]))
    print('rsq([4,4,3,6,7], [6,7,5,10,12]):', rsq([4,4,3,6,7], [6,7,5,10,12]))
    print('simple_regression([1,2,3,4,5], [5,4,3,2,1]):', simple_regression([1,2,3,4,5], [5,4,3,2,1]))
    # end of the test code


