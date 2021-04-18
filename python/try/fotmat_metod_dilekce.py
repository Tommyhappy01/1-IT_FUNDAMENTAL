matbu_form = """ 
Ad ve Soyad    : {} {}
Doğum Tarihi   : {}
Adres          : {}
Uzmanlık Alanı : {}
referans       : {}
Kısa öz geçmiş : {}
Yazılım mühendisliği alanında çalışmak istiyorum.
"""
ad = input("lütfen adınızı giriniz: ")
soyad = input("Lütfen soy adınızı giriniz: ")
d_tarihi = input("lütfen doğum tarihinizi gün ay yıl olarak giriniz: ")
adres = input("lütfen adres bilgilerinizi giriniz: ")
uzmanlik = input("uzmanlık alanlarınızı yazınız:")
referans = input("Referanslarınızı yazınız(torpil olarak değil): ")
oz_gecmis = input("kısa öz geçmişinizi giriniz: ")

print(matbu_form.format(ad, soyad, d_tarihi, adres, uzmanlik, referans, oz_gecmis ))
