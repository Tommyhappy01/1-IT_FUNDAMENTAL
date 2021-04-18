# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 07:10:07 2021

@author: MTM
"""

phrase = "Biz mükemmel %d milletiz %s öğretmenim." %(1, "değilmiyiz")
print(phrase)

a = "ali amca okula toplantı %s %d defa gitti,ama öğretmen yoktu." %("için",2)
print(a)
b = "İnşaallah %s okula %s %.2f gibi gideceğim %d saat kalacağım"%("sabah","toplantı için",2,3)
print(a,b,sep="\n")
print("%.11s"%b)
print("%.19s"%b)