# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:16:17 2021

@author: ÖKTEN
"""

a= {1:"one", 2 : 2, "string" : 2, False : [1,2,3], "c" : "3.14", (1,2): "clrswy"}
print(a)  #dict yaptık key str int tuple

xx = dict(bir="one",iki= "two")
print(xx)  # değişken atamadki gibi str olur

şehir = "istanbul"
şehir1 = "ankara"
nufüs = 1000
şehirler = {1:şehir,2:şehir1,  "nufüsum":nufüs}
print(şehirler)
print(şehirler[2]) # key neyse onu yaz

print(şehirler["nufüsum"]) # key neyse onu yaz  int geldi

state_capitals = {'Arkansas': 'Little Rock',
'Colorado': 'Denver',
'California': 'Sacramento',
'Georgia': 'Atlanta'}
state_capitals['Virginia'] = 'Richmond' # adding a new item
print(state_capitals)
