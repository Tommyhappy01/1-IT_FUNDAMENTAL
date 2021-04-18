# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:31:05 2021

@author: ÖKTEN
"""

#If we had bought $2000 crypto coins at the weekend, 
#we would have had $4,152.32 with a profit share of 
#11% after 5 days.

capital = 2000
total = "4.152.32"
rate = 11
duration = "5"
print"""If we had bought ${} crypto coins at the weekend,
we would have had ${} with a profit share of {}% after 
{} days.""" .format(capital, total, rate, duration)