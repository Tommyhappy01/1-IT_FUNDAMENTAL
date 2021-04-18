# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:23:24 2021

@author: ÖKTEN
"""

#  list_name =[index no]
#[liste][index]

word = ["h","a","p","p","y"]
print(word[1]) #index nosu 1 olanı ver
print(word[0])

colors = ["red","blue",["p",8],3, True]
print(colors[4]) 
print(type(colors[4]))#elemanı çekip çıkardı bool oldu
variable = colors[2]
print(type(variable))#listeyse liste........

şehirler = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
print(şehirler) #uzunluk 1 oldu tek eleman
print(şehirler[0])
print(type(şehirler))# liste tipi
print(şehirler[0][2])
print(type(şehirler[0][2][3]))# 0.liste 2. ele 3. karakter