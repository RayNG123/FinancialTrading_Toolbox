#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 9
#File Description: This file contain a base stock price stimulater using monte carlo
#simulation, which can be built as different types of option stimular pricing model.
#It can also return the result of the simulation as a plot and stimulate stock
#with different paramters

import numpy as np
import matplotlib.pyplot as plt
import math

class MCStockSimulator:
  """
  A User Defined Class of Stock Price with Monte Carlo Stimuation 
  """
  def __init__(self, s, t, mu, sigma, nper_per_year):
      """
      Initialize the stock price stimulator
      Data Include:
      s (the current stock price in dollars),
      t (the option maturity time in years),
      mu (the annualized rate of return on this stock),
      sigma (the annualized standard deviation of returns),
      nper_per_year (the number of discrete time periods per year)
      """
      self.s = s
      self.t = t
      self.mu = mu
      self.sigma = sigma
      self.nper_per_year = nper_per_year
      self.dt = 1/self.nper_per_year

  def __repr__(self):
      """
      Textual representation for the stock price stimulator
      """
      return f'MCStockSimulator (s=${self.s:.2f}, t={self.t:.2f} (years), mu={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year})'

  def generate_simulated_stock_returns(self):
      """
      generate_simulated_stock_returns(self) on your class MCStockSimulator, which 
      will generate and return a np.array (numpy array) containing a sequence of 
      simulated stock returns over the time period t
      """
      zs = np.random.normal(0, 1, int(self.nper_per_year*self.t))
      return np.array([(self.mu - (self.sigma**2)/2)*self.dt + z*self.sigma*self.dt**(1/2) for z in zs])

  def generate_simulated_stock_values(self):
      """
      generate and return a np.array (numpy array) containing a sequence of stock 
      values, corresponding to a random sequence of stock return. There are t * 
      nper_per_year discrete time periods, where t is the length of the simulation.
      """
      #initialize returns series
      returns = self.generate_simulated_stock_returns()

      #Exponentiate all values
      returns = [self.s] + list(np.exp(returns))

      #Cumulative product to get stock price
      return np.cumprod(returns)

  def plot_simulated_stock_values(self, num_trials = 1):
      """
      generate a plot of of num_trials series of simulated stock returns. num_trials is 
      an optional parameter; if it is not supplied, the default value of 1 will be used
      """
      #Initialize title, ylabel, xlabel
      plt.title(f'{num_trials} simulated trials')
      plt.xlabel('years')
      plt.ylabel('$ value')

      #Create xaxis dtaa
      xaxis = [self.dt*i for i in range(int(self.nper_per_year*self.t)+1)]

      #Iterate over to plot for each trial
      for _ in range(num_trials):
        plt.plot(xaxis,self.generate_simulated_stock_values())
      plt.show()