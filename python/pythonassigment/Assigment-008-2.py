# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:32:59 2021

@author: Joseph Forest
"""

# Assigment-008/2 
# Task 1 (Profit calculation)
sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  
# Formula: total_profit = (sell_value - cost_value) * inventory

# accessing cost_value, sell_value, inventory in sales
cost_value = sales["cost_value"]
sell_value = sales["sell_value"]
inventory = sales["inventory"]

# apply formula and profit calculation
total_profit = round((sell_value - cost_value) * inventory, 2)
total_profit = int(total_profit)
print("Total Profit: ", total_profit)

# the profit will be : 13130
result = 13130
if total_profit == result:
    print("Profit Calculation is True")
else:
    "you must have made a mistake! Please, try again"
    
# Task 2  (Payroll Format)    

    
