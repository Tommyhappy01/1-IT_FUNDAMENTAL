# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:38:35 2021

@author: Joseph Forest
"""

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

data = {i: numbers.count(i) for i in numbers}

frequent = max(data, key = data.get)
frequency = data[frequent]
print(f"the most frequent number is {frequent} and it was {frequency} times repeated")



