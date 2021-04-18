# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:32:30 2021

@author: ÖKTEN
"""

text ="tyou can learn almost everything in pre classz"
print(text.upper().strip("TZ"))
print(text.strip("tz").upper())

text1 = "In God wee Trust"
print(text1.replace("e","",1))

print(text1.replace("ee", "e").title())

print(text1.replace("wee", "We"))