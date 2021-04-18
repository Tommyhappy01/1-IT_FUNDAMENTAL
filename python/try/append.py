# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 21:46:58 2021

@author: ÖKTEN
"""
# append ekledi ekleyerek devam.
a = ["merhaba Türkiye"]
c = a.append("her nerede ")
b = a.append("yaşanıyor ve yaşatılıyorsa")
print(a)

# append ekledi ekleyerek devam. Boş klasörden başlıyor
a = []
c = a.append("her nerede ")
b = a.append("yaşanıyor ve yaşatılıyorsa")
print(a)

# append ekledi ekleyerek devam.
#insert index nosunu verince ekledi.
#¿0123456
şehir = ["Kastamonu","Yozgat","Niğde","Afyon"]
şehir.append("Adana merkez çatlıyor herkes")
şehir.insert(3,"Newyork Chicago Miami")
#remove çıkardı
şehir.remove("Afyon")
print(şehir)
