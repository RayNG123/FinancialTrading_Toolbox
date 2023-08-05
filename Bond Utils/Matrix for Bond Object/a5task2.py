#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#name: Yusen Wu
#Email: wuyusen@bu.edu
#Assigment: 4
#File Description: This file contains conde for a user defined class BondPortfolio, 
#and a set of functions to to print out and process related statistics for a list
#of Bonds as a whole. like toal maturity value, total convexity and total duration. 
#The class will also be able to print out related statistics of each individual


from a5task1 import *

class BondPortfolio:
  """
  A User defined class Bondportfolio that incorporate a list of functions
  that can store a list of Bond class, process them as a whole, and print 
  out corresponding statistics of the entire portfolio and each of the Bond
  """ 
  def __init__(self):
    """
    Initialize BondPortfolio class and bond list
    """
    self.__bond_list = []

  def __repr__(self):
    """
    return a text representation for the bond portfolio
    """
    string = f'BondPortfolio contains {len(self.__bond_list)} bonds:'

    #Iterate over each bond to print out related statistics
    for bond in self.__bond_list:
        string += '\n\n'
        string += bond.__repr__()
    string += '\n'

    #Print Portfolio value
    string += '\n'
    string += f'Portfolio value:              ${self.get_value():.2f}'

    #Print Portfolio yield to maturity
    string += '\n'
    string += f'Portfolio yield to maturity:  {self.get_yield_to_maturity():.4%}'

    #Print Portfolio duration
    string += '\n'
    string += f'Portfolio duration:           {self.get_duration():.2f}'

    #Print Portfolio convexity
    string += '\n'
    string += f'Portfolio convexity:          {self.get_convexity():.2f}'
    return string

  def add_bond(self, b):
    """
    Add a bond to the portfolio
    """
    assert isinstance(b, Bond), f'Only data type Bond can be added to data type BondPortfolio'
    self.__bond_list.append(b)

  def rem_bond(self, b):
    """
    Delete a bond from the portfolio
    """
    self.__bond_list.remove(b)

  def get_value(self):
    """
    Get the total value of the portfolio
    """
    return sum([i._Bond__price for i in self.__bond_list])

  def get_yield_to_maturity(self):
    """
    Get the yield to maturity of the portfolio
    """
    if len(self.__bond_list) == 0:
        return 0
    else:
        return sum([i._Bond__price*i._Bond__yield_to_maturity for i in self.__bond_list])/self.get_value()

  def get_duration(self):
    """
    Get the duration of the portfolio
    """
    if len(self.__bond_list) == 0:
        return 0
    else:
        return sum([i._Bond__price*i.get_duration() for i in self.__bond_list])/self.get_value()

  def get_convexity(self):
    """
    Get the convexity of the portfolio
    """
    if len(self.__bond_list) == 0:
        return 0
    else:
        return sum([i._Bond__price*i.get_convexity() for i in self.__bond_list])/self.get_value()

  def shift_ytm(self, delta_ytm):
    """
    Uniformly change ytm for all bond in the portfolio
    """
    #Iterate over bonlist to change ytm of each
    for bond in self.__bond_list:
      bond.set_yield_to_maturity(bond._Bond__yield_to_maturity + delta_ytm)
     