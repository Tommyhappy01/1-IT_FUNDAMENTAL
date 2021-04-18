# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 12:25:14 2021

@author: MTM
"""

isim = "serdar"
print(isim.rindex("s"))
print("""
      index ve rindex kendisine parametre olarak verilen harfi bulamazsa: 
         " ValueError: substring not found" hatasını veriyor. Böyle bir hata 
         almamak çin find ve rfinf metotlarını kullanabilriiz. \n
      """)

txt = "Hello World"
print(txt.find("j"))

print("""
      find ve rfind metotları kendisine verilen parametreyi bulamazsa 
      -1 değer döndürür.
      """)
# diğer tüm özellikleri index ile ortak