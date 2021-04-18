# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:53:38 2021

@author: MTM
"""

text = "www.clarusway.com.tr"
print(text.endswith("com.tr"))
print(text.startswith("www.c"))

email = "clarusway@clarusway.com is my e-mail adress"
print(email.startswith("u",14))
print(email.endswith("m",18,23))

sentence = "I live and work in İsKilipli"

print(sentence.upper())  

print(sentence.lower())#küçük

print(sentence.swapcase())#değiştir

print(sentence) 
print(sentence.title())
replace_sentence = sentence.replace("i","ı")
swap_case = sentence.swapcase()
print(replace_sentence)
print(swap_case)
print(sentence.capitalize())

