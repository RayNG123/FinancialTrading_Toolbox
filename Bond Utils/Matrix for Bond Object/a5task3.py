#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 4
#File Description: This file contains conde for a user defined class Mortage, 
#and a set of functions to to print out and process related statistics like
#maturity value, time, payment and frequency, price and yield to maturity,
#convexity and duration.

from a5task1 import *
from a5task2 import *

class Mortgage(Bond):
    
    def __init__(self, original_value, maturity_time, ann_pct_rate, coupon_frequency=12):
      """
      Initialize a Mortgage Class and all data members
      """
      #Initiate Super Class
      super().__init__(0, maturity_time, ann_pct_rate, coupon_frequency)
        
      #Initiate Specific data members
      self.__original_value = original_value
      self._Bond__price = original_value

    def __repr__(self):
      """
      return a text representation for the mortgage
      """
      return f"""${self.__original_value:.2f}-original value, {self._Bond__maturity_time}-year, 
             {self.get_coupon_rate():.4%} APR mortgage bond: \npayment=${self.get_coupon_amount():.2f}, 
             price=${self.get_price():.2f}, {self.get_price()/self.__original_value:.4%} of par 
             ytm={self.get_yield_to_maturity():.2%}, duration={self.get_duration():.4f}, 
             convexity={self.get_convexity():.4f}"""

    def get_original_value(self):
      """
      Get the original value of the mortgage
      """
      return self.__original_value

    def get_coupon_amount(self):
      """
      return the coupon payment of the mortgage
      """
      #Get APR and number of periods
      r = self.get_coupon_rate()/self.get_coupon_frequency()
      n = self.get_maturity_time() * self.get_coupon_frequency()

      return self.__original_value*r*(1 + r)**n/((1 + r)**n - 1)

    def get_duration(self):
      """
      return the duration of the mortgage
      """
      return bond_duration(self.__original_value, 
                           self._Bond__coupon_rate,
                           self._Bond__maturity_time, 
                           self._Bond__coupon_frequency, 
                           self._Bond__yield_to_maturity,
                           'Mortgage')
        
    def get_convexity(self):
      """
      return the convexity of the mortgage
      """
      return bond_convexity(self.__original_value, 
                            self._Bond__coupon_rate,
                            self._Bond__maturity_time, 
                            self._Bond__coupon_frequency, 
                            self._Bond__yield_to_maturity,
                            'Mortgage')