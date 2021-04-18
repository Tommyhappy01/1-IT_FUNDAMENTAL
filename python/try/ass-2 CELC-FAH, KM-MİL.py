# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:48:34 2021

@author: MTM
"""

#1 °F'lik bir sıcaklık farkı, 
#0,556 °C'lik bir sıcaklık farkına eşittir.

#Fahrenheit biriminden Celsius birimine dönüştür
#℃ =℉ - 32 / 1.8000

celsius = input("Please input celsius degree:")
fahrenheit = int(celsius)*1.8 + 32

print("{} celsius = {} fahrenheit.".format(celsius,fahrenheit))
print(f"{celsius} celsius = {round(fahrenheit)} fahrenheit.")

# km/ mil dönüşüm işlemi

km = input("Km cinsinden değer giriniz:")
mil = int(km)*0.63
print(f"{km} km = {round(mil,2)} mil dir.")