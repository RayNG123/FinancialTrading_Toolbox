#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:15:40 2023
name: Yusen Wu
Email: wuyusen@bu.edu
Assigment: 1
"""

from a2task1 import *
from a2task2 import *

def collect_bids(filename):
  """
  process the data file containing the bids.
  """
  result = []
  with open(filename, 'r') as bids:
    for id, bid in enumerate(bids):
      if id != 0:
        bid = bid[:-1]
        fields = [i.strip() for i in bid.split(',')]
        fields[0] = int(fields[0])
        fields[1] = int(fields[1])
        fields[2] = float(fields[2])
        result.append(fields)
  return result

def print_bids(bids): 
  """
  to process the a of bids, and produce a beautifully-formatted table of the bids
  """
  print(f'  Bid ID          Bid Amount           Price')
  for bid in bids:
    id, amount, price = bid
    print(f'  {id:6d}        ${amount:12d}    ${price:12.3f}')

def find_winning_bids(bids, total_offering_fv, c, n, m):
  """
  processes a list of bids and determine which are successful in the auction
  """
  print(f'Here are all the bids:')
  print_bids(bids)
  print('\t')

  print(f'Here are all of the bids, sorted by price descending:')
  bids = sorted(bids, reverse = True, key = lambda x: (x[2], x[1]))
  print_bids(bids)
  print('\t')

  print(f'The auction is for ${total_offering_fv:.2f} of bonds.')
  print('\t')

  bids_result = [i[:] for i in bids]
  count_offering = 0

  for i, bid in enumerate(bids_result):
    count_offering += bid[1]
    if count_offering >= total_offering_fv:
      diff = count_offering - total_offering_fv
      bid[1] = bid[1] - diff
      clear_index = i
      break
    else:
      clear_index = len(bids_result) - 1

  if clear_index is not len(bids_result) - 1:
    for i, bid in enumerate(bids_result):
      if i > clear_index:
        bid[1] = 0

  clear_price = bids_result[clear_index][2]
  ytm = bond_yield_to_maturity(100, c, n, m, clear_price)

  print(f'{clear_index + 1} bids were successful in the auction.')
  print(f'The auction clearing price was ${clear_price:.3f}, i.e., YTM is {ytm:.6f} per year.')
  print(f'Here are the results for all bids:')
  print('\t')

  print_bids(bids_result)
  
  return bids_result

if __name__ == '__main__':

    bids = collect_bids('./bond_bids.csv')
    print("Here are all the bids:")
    print_bids(bids)
    print()

    processed_bids = find_winning_bids(bids, 500000, 0.03, 5, 2)