# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 08:08:43 2021

@author: MTM
"""
x = "HelloWorld!"
print('%.5s' % x) 

phrase = "I have %d %s and %.2f brothers" %(4,"children",5)
print(phrase)               #burda d: numeric s: string f: float .2 (2 ondalık)
                            #dddd sssss ffff unutma
                            
meyve= "elma %.5s %d kilosu %.3f tl armutta hediye." %("çok güzel", 3555, 15) 
print(meyve)
telefon = "Mevcut: %d samsung %d huaweı ve %.6f ıphone" %(3,5,3)
print(telefon)

sentence = "apologizing is a virtue"  #burda % .3 s = stringde ilk üçü al 
print("%.4s" %sentence)                 # d yemedi, s ve float ta oldu
                                        #zaten floatta , sonrasının kaç ola...
print("%d pounds of %s left" %(33, "bananas"))