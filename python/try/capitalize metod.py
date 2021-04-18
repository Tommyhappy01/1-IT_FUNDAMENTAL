# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:24:26 2021

@author: MTM
"""

print("""
      capitalize metedu karakter dizileri üzerinde değişiklik yapar. 
      karakter dizisinin ilk harfini büyük yapar. upper() karakter dizisinin
      tamamını büyük yaparken, lower() karakter dizisinin tamamını küçük yapar.
      startswith() dizinin ilk harfini sorgularken endswith() dizinin son 
      harfini sorgular. Örneklerimizi yapalım
      
      """)
isim = "serdar"     
metin = f"""bu bir deneme metnidir. 
    lower fonksiyonu çıktısı {isim.lower()}
    upper() metodu çıktısı: {isim.upper()}
    startswith metodu çıktısı {isim.startswith("s")}
    endswith metodu çıktısı: {isim.endswith("r")}
    capitalize metodu çıktısı: {isim.capitalize()}"""
print(metin)    

print(""" Önemli Not:
      capitalize() metodu ile i sesi çeirilirken "I" olarak
      çevirilir. Bu yüzden string işlemlerinde Türkçe karakter i dikkate 
      almamız gerekir. şimdi ilk harfi i olan şehirler için bir uygulama
      yapalım.
           """)
print()           
şehir = input("lütfen bir i ile başlayan bir şehir giriniz")           
if şehir.startswith("i"):
    şehir = şehir.replace("i","İ",1)
    print(şehir)
else:
    print(şehir.capitalize())
