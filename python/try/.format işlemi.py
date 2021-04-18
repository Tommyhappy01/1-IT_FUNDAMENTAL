# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:13:18 2021

@author: MTM
"""

x= "üzüm"    #str.format()değerleri sırayla atadı
y= "karpuz"
z= 15.5
print( "Satın aldığımız ürünler {} kilolar ise{}" .format(x +y,z))

print("{şehir} {ülke}'nin en {sıfat} şehridir." .format(şehir="islambul", ülke= "Türkiye", sıfat="kalabalık"))
print("{şehir} {ülke}'nin en {özellik} şehridir." .format(şehir="Muş", ülke="Türkiye", özellik="güzel"))

print("{6} {0} {5} {3} {4} {1} {2}".format("have",6,"monts.","a job","in","found", "I will"))

