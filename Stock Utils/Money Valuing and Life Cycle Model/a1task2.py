#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:04:40 2023
name: Yusen Wu
Email: wuyusen@bu.edu
Assigment: 1
"""

from a1task1 import *

def dollar_format(amount):
    """
    takes a parameter amount which is a number, and returns 
    a beautifully-formatted string of dollars and cents, 
    including the dollar sign and comma-separated thousands and millions
    """
    return f'${amount:12,.2f}'

def life_cycle_model():
    """
    will interact with the user to collect inputs and display outputs
    """
    print('Welcome to the Life-Cycle Sustainable Spending Calculator.')
    print('\t')

    rate_of_return = float(input("Enter the current inflation-indexed risk-free rate of return:"))
    age = int(input("Enter your age now:"))
    retirement_age = int(input("Enter your expected retirement age:"))
    income = float(input("Enter your current annual income:"))
    print('\t')

    remaining_working_years = retirement_age - age
    pv_human_cap = pv_annuity(rate_of_return, remaining_working_years, income)
    print(f'You have {remaining_working_years} remaining working years with an income of {dollar_format(income)} per year.')
    print(f'The present value of your human capital is about {dollar_format(pv_human_cap)}')
    print('\t')

    assets = float(input("Enter the value of your financial assets:"))
    economic_net_worth = assets + pv_human_cap
    print(f'Your economic net worth is: {dollar_format(economic_net_worth)}')
    print('\t')

    years_of_consumption = 100 - age
    consumption = annuity_payment(rate_of_return, years_of_consumption, economic_net_worth)
    print(f'Your sustainable standard of living is about {dollar_format(consumption)} per year.')
    savings = income - consumption
    print(f'To achieve this standard of living to age 100, you must save {dollar_format(savings)} per year.')
    print('\t')

    print('Here is a annual summary of your financial plan:')
    print('\t')
    print('Age    Income         Consumption    Saving         Assets')
    for i in range(remaining_working_years):
      age += 1
      assets = assets * (1 + rate_of_return) + savings
      print(f"{age}{' '*(6 - len(str(age)))} {dollar_format(income)}  {dollar_format(consumption)}  {dollar_format(savings)}  {dollar_format(assets)}")
    for i in range(years_of_consumption - remaining_working_years):
      age += 1
      income = 0
      savings = -consumption 
      assets = assets * (1 + rate_of_return) + savings
      print(f"{age}{' '*(6 - len(str(age)))} {dollar_format(income)}  {dollar_format(consumption)}  {dollar_format(savings)}  {dollar_format(assets)}")

if __name__ == '__main__':
 # call the function:
  life_cycle_model()