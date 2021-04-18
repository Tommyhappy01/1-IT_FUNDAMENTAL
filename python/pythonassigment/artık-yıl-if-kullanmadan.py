# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:39:29 2021

@author: Joseph Forest
"""
print(""" Artık yıl hesaplama programına hoşgediniz.
 True artık yıl, 
 False Artık yıl değil anlamına gelir.   """)
yıl = int(input("lütfen artık yıl sorgulaması için bir yıl giriniz. "))

a = yıl % 400 == 0 
b = yıl % 100 != 0
c = yıl % 4 == 0
artık_yıl = b and c or  a
print(artık_yıl)