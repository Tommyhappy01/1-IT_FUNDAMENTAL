# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:32:53 2021

@author: Joseph Forest
"""

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

# Finds out the most frequent number in the given list.
frequent = max(numbers, key = numbers.count)

# Calculates its frequency.
frequency = numbers.count(frequent)

# Prints out the result such as below: 
# --> 'the most frequent number is 3 and it was 4 times repeated'
print(f"the most frequent number is {frequent} and it was {frequency} times repeated")


