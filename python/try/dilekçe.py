# -*- coding: utf-8 -*- 
"""
Created on Tue Mar 16 14:58:21 2021

@author: MTM
"""

# Matbu dilekçe formu
import datetime
kurum = input("Kurum bilgilerini giriniz:")
adı = input("Adınızı giriniz:")
soyadı = input("Soyadınızı giriniz:")
tc = input("T.C. Kimlik numaranızı giriniz:")
sicili = input("Sicil bilgilerinizi giriniz:")
adres = input("Adresinizi giriniz:")
i_tarih = input("İzin tarihlerinizi giriniz:")
tarih = datetime.datetime.now()

print(f"""
      Adı:{adı}
      Soyadı:{soyadı}
      TC kimlik no:{tc}
      Sicili:{sicili}
      Adresi:{adres}
      Tarih:{tarih}
             
      
                Yıllık iznimi {i_tarih} tarihleri arasında belirttiğim 
                {adres} adresinde geçirmek istiyorum, 
                gereğini arz ederim.{tarih.strftime("%x")}""")
                
print("""Yıllık iznimi {} tarihleri arasında belirttiğim {} adresinde 
      geçirmek istiyorum, gereğini arz ederim.{}""".format(i_tarih, adres, tarih))