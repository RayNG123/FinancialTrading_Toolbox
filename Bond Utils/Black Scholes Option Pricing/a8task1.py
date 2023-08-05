#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 8
#File Description: This file contains a set of user defined class to build a black
#shole priceing formula for an option

from scipy.stats import norm
import math

class BSMOption:
  """
  a user defined class that encapsulates the data required to do Black-Scholes option pricing formula
  """
  def __init__(self, s, x, t, sigma, rf, div):
      """
      parameters required to initiate the class
      """
      self.s = s
      self.x = x
      self.t = t
      self.sigma = sigma
      self.rf = rf
      self.div = div

  def __repr__(self):
      """
      textual representation of the option
      """
      return f's = ${self.s:.2f}, x = ${self.x:.2f}, t = {self.t:.2f} (years), sigma = {self.sigma:.3f}, rf = {self.rf:.3f}, div = {self.div:.2f}'

  def d1(self):
      """
      calculate and return d1 value of the option
      """
      a = math.log(self.s/self.x)
      b = (self.rf - self.div + 0.5*self.sigma**2)*self.t
      c = self.sigma*self.t**(1/2)
      return (a+b)/c

  def d2(self):
      """
      calculate and return d2 value of the option
      """
      return self.d1() - self.sigma*self.t**(1/2)

  def nd1(self):
      """
      calculate and return nd1 probability of the option
      """
      return norm.cdf(self.d1())

  def nd2(self):
      """
      calculate and return nd2 probability of the option
      """
      return norm.cdf(self.d2())

  def value(self):
      """
      calculate and return the value of the option
      """
      print("Cannot calculate value for base class BSMOption.")
      return 0

  def delta(self):
      """
      calculate and return the delta of the option
      """
      print("Cannot calculate delta for base class BSMOption.")
      return 0



class BSMEuroCallOption(BSMOption):
  """
  a user defined class that encapsulates the data required to do Black-Scholes option 
  pricing formula for a euro call option
  """
  def __init__(self, s, x, t, sigma, rf, div):
      """
      Initialize all parameters needed
      """
      super().__init__(s, x, t, sigma, rf, div)

  def value(self):
      """
      calculate and return the value of the option
      """
      return self.s*math.exp(-self.div*self.t)*self.nd1() - self.x*math.exp(-self.rf*self.t)*self.nd2()

  def delta(self):
      """
      calculate and return the delta of the option
      """
      return math.exp(-self.div*self.t)*self.nd1()

  def __repr__(self):
      """
      textual representation of the option
      """
      return f'BSMEuroCallOption, value = ${self.value():.2f},\nparameters = (s = ${self.s:.2f}, x = ${self.x:.2f}, t = {self.t:.2f} (years), sigma = {self.sigma:.3f}, rf = {self.rf:.3f}, div = {self.div:.2f})'



class BSMEuroPutOption(BSMOption):
  """
  a user defined class that encapsulates the data required to do Black-Scholes option 
  pricing formula for a euro put option
  """
  def __init__(self, s, x, t, sigma, rf, div):
      """
      Initialize all parameters needed
      """
      super().__init__(s, x, t, sigma, rf, div)

  def value(self):
      """
      calculate and return the value of the option
      """
      return self.x*math.exp(-self.rf*self.t)*(1-self.nd2()) - self.s*math.exp(-self.div*self.t)*(1-self.nd1())

  def delta(self):
      """
      calculate and return the delta of the option
      """
      return -math.exp(-self.div*self.t)*(1-self.nd1())

  def __repr__(self):
      """
      textual representation of the option
      """
      return f'BSMEuroCallOption, value = ${self.value():.2f},\nparameters = (s = ${self.s:.2f}, x = ${self.x:.2f}, t = {self.t:.2f} (years), sigma = {self.sigma:.3f}, rf = {self.rf:.3f}, div = {self.div:.2f})'