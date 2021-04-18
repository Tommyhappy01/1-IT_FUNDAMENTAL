# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 13:26:21 2021

@author: ÖKTEN
"""


# Group Anagrams: example:
# ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:[["ate","eat","tea"], ["nat","tan"], ["bat"]]  


"""Tamam, oncelikle bos bir dict olusturuyoruz,
Bunu liste icinde her bir grup icin kullanacagiz
sonra liste icinde her bir string'i loop a sokuyoruz, ama sorted ederek
boylece anagram olan stringler birbirine esit oluyor
sonra conditional eklemeler yapacagiz
eger bu sort edilen string dict icinde varsa, string'in ilk halini value olarak ekle diyoruz
eger yoksa yeni bir key ekle
ve bu string'i value olarak ekle diyoruz
ilk ornekte mesela
eat
sorted('eat')
a, e , t olur
dict icinde olmadigi icin key olarak, eat hali de value olarak ekleniyor
sonra tea de a, e, t olur sorted yapinca
bu dict icinde oldugu icin dict'e yeni bir key eklemeden append yapiliyor, tea haliyle
en son dict'in value'lari liste halinde cikti aliniyor
burada sorted_string key
string ise value"""
 lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Python3 program for the above approach
def group_anagrams(lst):
    grouped_anagrams = {}
    for string in lst:
        sorted_string = str(sorted(string))
        if sorted_string in grouped_anagrams:
            grouped_anagrams[sorted_string].append(string)
        else:
            grouped_anagrams[sorted_string] = [string]
    return list(grouped_anagrams.values())