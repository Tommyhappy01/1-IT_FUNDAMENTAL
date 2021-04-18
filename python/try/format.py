# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:21:47 2021

@author: ÖKTEN
"""

phrase = "{2} {3} {1} {0}".format("circumstances","in all","generosty", "wins")
print(phrase)
condition = "circumstances"
morality ="generosty"
phrase = "{morality} {1} {0} {condition}".format("in all", "wins",condition = "circumstances", morality ="generosty")
print(phrase)
