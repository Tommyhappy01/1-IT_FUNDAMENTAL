# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:00:42 2021

@author: MTM
"""

# önce while döngüsü ile bir örnek yapalım. 
# bir karakter dizisini alt alta yazdırmak için
# while döngüsünü kullanalım.

tr_harfler = "çşöğüıİ"  # Türkçe karakterler 
a = 0  # döngünün bir koşula bağlı olması için bir referans belirledik
while a < len(tr_harfler):
    print(tr_harfler[a])
    a += 1

print("şimdi aynı işlemi for döngüsü ile yapalım")

for i in tr_harfler:
    print(i)

print("""
      
      for döngüsü ile while çalışma mantığı olarak farklıdırlar.
      while döngü iterasyonunu kendisine verilen koşulun true ve false olma
      durumuna göre yapar. Yani koşul sağlandığı sürece çalışmaya devam eder.
      fakat for kendisine verielen data dizisinde yer alan her öğenin 
      üzerinden tek tek geçer ve işlem yapar.
      
      """)
      
rakamlar = "1234567890"  # integer nesne üzerinde döngü kurulmaz  


#for i in rakamlar:
#    print(i) hata verir çalışmaz. 
#'int' object is not iterable
#int nesne üzerinde döngü kurulamaz hatasını alırız
#

for i in rakamlar:
    print(i, end = " ")

print("aynı çıktıyı while döngüsü ile yapalım")
sayac = 0
while sayac < len(rakamlar):
    print(rakamlar[sayac], end =" ")
    sayac += 1 # döngü her başa döndüğünde sayaç bir arttır
    
