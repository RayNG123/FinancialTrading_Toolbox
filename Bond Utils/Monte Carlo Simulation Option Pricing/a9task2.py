#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 9
#File Description: This file contains a sets of option pricing stimulater all inhereted from
#a stock price stimulator, including put and call option stimulator pricing for euro, asia, and
#and look back type option. All option pricing stimulater can estimate the value of the option using
#different number of trials and report related statistics

import numpy as np
from a9task1 import *

class  MCStockOption(MCStockSimulator):
  """
  A User defined class of stock option stimulator inhereited from MCStockSimulator
  """
  def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
      """
      Initialize the stock option stimulator
      Data Includ:
      s, which is the initial stock price
      x, which is the option’s exercise price
      t, which is the time to maturity (in years) for the option
      r, which is the annual risk-free rate of return
      sigma, which is the annual standard deviation of returns 
        on the underlying stock
      nper_per_year, which is the number of discrete time periods 
        per year with which to evaluate the option, and
      num_trials, which is the number of trials to run when calculating 
        the value of this option
      """
      super().__init__(s, t, r, sigma, nper_per_year)
      self.x = x
      self.num_trials = num_trials

  def __repr__(self):
      """
      Textual representation for the stock option stimulator
      """
      return f'MCStockOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'

  def value(self):
      """
      return the value of the option. This method cannot be concretely implemented 
      in this base class, but will be overridden in each subclass (see below)
      """
      print('Base class MCStockOption has no concrete implementation of .value().')
      return 0

  def stderr(self):
      """
      return the standard error of this option’s value. The standard error is calculated 
      as stdev / sqrt(num_trials), where stdev is the standard deviation of the values 
      obtained from many trials.
      can only be calculated after running some trials
      """
      if 'stdev' in dir(self):
        return self.stdev / math.sqrt(self.num_trials)
      return 0

class MCEuroCallOption(MCStockOption):
  """
  A User defined class of euro call option stimulator inhereited from MCStockOption
  """
  def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
      """
      initialize the stimulator
      Data needed is the same as MCStockOption
      """
      super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

  def __repr__(self):
      """
      Textual representation for the stock option stimulator
      """
      return f'MCEuroCallOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'

  def value(self):
      """
      Calculate the mean and stdev of the option under different trials, and
      return the mean
      """
      #Get stock prices
      trials = [self.generate_simulated_stock_values()[-1] for i in range(self.num_trials)]
      
      #Get option prices
      trials = [max(i - self.x, 0)*math.exp(-self.mu*self.t) for i in trials]

      #Calculate statistics 
      self.means = np.mean(trials)
      self.stdev = np.std(trials)
      return self.means

class MCEuroPutOption(MCStockOption):
  """
  A User defined class of euro put option inhereited from MCStockOption
  """
  def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
      """
      initialize the stimulator
      Data needed is the same as MCStockOption
      """
      super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

  def __repr__(self):
      """
      Textual representation for the stock option stimulator
      """
      return f'MCEuroPutOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'

  def value(self):
      """
      Calculate the mean and stdev of the option under different trials, and
      return the mean
      """
      #Get stock prices
      trials = [self.generate_simulated_stock_values()[-1] for i in range(self.num_trials)]

      #Get option prices
      trials = [max(self.x-i, 0)*math.exp(-self.mu*self.t) for i in trials]

      #Calculate statistics 
      self.means = np.mean(trials)
      self.stdev = np.std(trials)
      return self.means

class MCAsianCallOption(MCStockOption):
  """
  A User defined class of asia call option inhereited from MCStockOption
  """
  def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
      """
      initialize the stimulator
      Data needed is the same as MCStockOption
      """
      super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

  def __repr__(self):
      """
      Textual representation for the stock option stimulator
      """
      return f'MCAsianCallOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'

  def value(self):
      """
      Calculate the mean and stdev of the option under different trials, and
      return the mean
      """
      #Get stock prices
      trials = [np.mean(self.generate_simulated_stock_values()) for i in range(self.num_trials)]

      #Get option prices
      trials = [max(i-self.x, 0)*math.exp(-self.mu*self.t) for i in trials]

      #Calculate statistics 
      self.means = np.mean(trials)
      self.stdev = np.std(trials)
      return self.means

class MCAsianPutOption(MCStockOption):
  """
  A User defined class of asia put option inhereited from MCStockOption
  """
  def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
      """
      initialize the stimulator
      Data needed is the same as MCStockOption
      """
      super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

  def __repr__(self):
      """
      Textual representation for the stock option stimulator
      """
      return f'MCAsianPutOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'

  def value(self):
      """
      Calculate the mean and stdev of the option under different trials, and
      return the mean
      """
      #Get stock prices
      trials = [np.mean(self.generate_simulated_stock_values()) for i in range(self.num_trials)]

      #Get option prices
      trials = [max(self.x-i, 0)*math.exp(-self.mu*self.t) for i in trials]

      #Calculate statistics 
      self.means = np.mean(trials)
      self.stdev = np.std(trials)
      return self.means
  
class MCLookbackCallOption(MCStockOption):
  """
  A User defined class of look back call option inhereited from MCStockOption
  """
  def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
      """
      initialize the stimulator
      Data needed is the same as MCStockOption
      """
      super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

  def __repr__(self):
      """
      Textual representation for the stock option stimulator
      """
      return f'MCLookbackCallOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'

  def value(self):
      """
      Calculate the mean and stdev of the option under different trials, and
      return the mean
      """
      #Get stock prices
      trials = [np.max(self.generate_simulated_stock_values()) for i in range(self.num_trials)]

      #Get option prices
      trials = [max(i-self.x, 0)*math.exp(-self.mu*self.t) for i in trials]

      #Calculate statistics 
      self.means = np.mean(trials)
      self.stdev = np.std(trials)
      return self.means

class MCLookbackPutOption(MCStockOption):
  """
  A User defined class of look back put option inhereited from MCStockOption
  """
  def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
      """
      initialize the stimulator
      Data needed is the same as MCStockOption
      """
      super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

  def __repr__(self):
      """
      Textual representation for the stock option stimulator
      """
      return f'MCLookbackPutOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'

  def value(self):
      """
      Calculate the mean and stdev of the option under different trials, and
      return the mean
      """
      #Get stock prices
      trials = [np.min(self.generate_simulated_stock_values()) for i in range(self.num_trials)]

      #Get option prices
      trials = [max(self.x-i, 0)*math.exp(-self.mu*self.t) for i in trials]
      
      #Calculate statistics 
      self.means = np.mean(trials)
      self.stdev = np.std(trials)
      return self.means