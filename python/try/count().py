# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:55:34 2021

@author: MTM
"""

print("""
      count() metedu ile bir karakter dizisinde vereceğimiz bir harfin kaç
      defa geçeceğini bulabiliriz. sonrasında bir program ile kullanıcıdan 
      aldığımız bir kelimenin içinde her harfin kaç defa geçtiğini bulalım
      """)
harf_listesi = ""
kelime = input("bir kelime giriniz")
for i in kelime:
    if i not in harf_listesi:
        harf_listesi += i
for i in harf_listesi:
    print(f"{i} harfi {kelime} kelimesinde {kelime.count(i)} defa geçiyor")
    
print("""
      şimdi count() metodu iki tane param
      """)