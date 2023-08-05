#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 4
#File Description: This file contains conde for a user defined class Bond, 
#and a set of functions to to print out and process related statistics like
#maturity value, time, coupon rate and frequency, price and yield to maturity,
#convexity and duration.

from help import *

class Bond:
  """
  A User defined class Bond that incoporates a list of functions 
  to process and represent a Bond and its correponding statistics
  """ 
  def __init__(self, 
               maturity_value, 
               maturity_time, 
               coupon_rate = 0, 
               coupon_frequency = 2):
    """
    initialize a new Bond object of this class
    """
    #Initialize All Data Members
    self.__maturity_value = maturity_value
    self.__maturity_time = maturity_time
    self.__coupon_rate = coupon_rate
    self.__coupon_frequency = coupon_frequency
    self.__price = maturity_value
    self.__yield_to_maturity = coupon_rate

  def __repr__(self):
    """
    return a beautifully-formatted string 
    representation of the Bond object
    """
    return f"""${self.__maturity_value:.2f}-maturity {self.__maturity_time}-year 
{self.__coupon_rate:.4%} bond, price=${self.__price:.2f}, 
ytm={self.__yield_to_maturity:.4%}, duration={self.get_duration():.4f}, 
convexity={self.get_convexity():.4f}"""

  def get_maturity_value(self):
    """
    get maturity value
    """
    return self.__maturity_value

  def get_maturity_time(self):
    """
    get maturity time
    """
    return self.__maturity_time

  def get_coupon_rate(self):
    """
    get coupon rate
    """
    return self.__coupon_rate

  def get_coupon_amount(self):
    """
    get coupon amount
    """
    return self.__coupon_rate*self.__maturity_value/self.__coupon_frequency

  def get_coupon_frequency(self):
    """
    get coupon frequency
    """
    return self.__coupon_frequency

  def get_price(self):
    """
    get price
    """
    return self.__price

  def get_yield_to_maturity(self):
    """
    get yield to maturity
    """
    return self.__yield_to_maturity

  def get_pmt_times(self):
    """
    get payment times
    """
    return cashflow_times(self.__maturity_time,
                          self.__coupon_frequency)

  def get_cashflows(self):
    """
    get cashflows list
    """
    return bond_cashflows(self.__maturity_value, 
                          self.__coupon_rate, 
                          self.__maturity_time, 
                          self.__coupon_frequency)
    
  def get_discount_factors(self):
    """
    get discount factors list
    """
    return discount_factors(self.__yield_to_maturity, 
                            self.__maturity_time, 
                            self.__coupon_frequency)
    
  def calculate_price(self):
    """
    Helper function to recalculate price when given new ytm
    """
    return bond_price(self.__maturity_value, 
                      self.__coupon_rate, 
                      self.__maturity_time, 
                      self.__coupon_frequency,
                      self.__yield_to_maturity)
    
  def set_yield_to_maturity(self, new_ytm):
    """
    Reset yield to maturity and corresponding price
    """
    self.__yield_to_maturity = new_ytm
    self.__price = self.calculate_price()

  def calculate_yield_to_maturity(self, accuracy=0.0001):
    """
    Helper function to recalculate ytm when given new price
    """
    return bond_yield_to_maturity(self.__maturity_value, 
                                  self.__coupon_rate,
                                  self.__maturity_time,
                                  self.__coupon_frequency, 
                                  self.__price, 
                                  accuracy = accuracy)

  def set_price(self, price):
    """
    Reset price and corresponding yield to maturity
    """
    self.__price = price
    self.__yield_to_maturity = self.calculate_yield_to_maturity()

  def get_duration(self):
    """
    Calculate the bond duration
    """
    return bond_duration(self.__maturity_value, 
                         self.__coupon_rate,
                         self.__maturity_time, 
                         self.__coupon_frequency, 
                         self.__yield_to_maturity)
    
  def get_convexity(self):
    """
    Calculate the bond convexity
    """
    return bond_convexity(self.__maturity_value, 
                          self.__coupon_rate,
                          self.__maturity_time, 
                          self.__coupon_frequency, 
                          self.__yield_to_maturity)