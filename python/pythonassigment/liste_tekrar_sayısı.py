# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:38:35 2021

@author: Joseph Forest
"""

numara = [1, 3, 7, 4, 3, 0, 3, 6, 3]

data = {i: numara.count(i) for i in numara}

frequent = max(data, key = data.get)
frequency = data[frequent]
print("the most frequent number is {} and it was {} times repeated".format(frequent,frequency))



