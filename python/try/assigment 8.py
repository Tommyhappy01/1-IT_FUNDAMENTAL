# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:52:20 2021

@author: C8381-tommy
"""
print("""###################################
  #                                #
       WELCOME TO PROFİT 
           PROGRAM 
  #################################
""")

sales = { "cost_value": 31.87,
          "sell_value": 45.00,
          "inventory": 1000    }  
cost = (sales["cost_value"])
sell = (sales["sell_value"])
inventory = (sales["inventory"])
print("inventory",(round((sell-cost) *inventory)),"dollar")



