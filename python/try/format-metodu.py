aciklama = """
Format metodu ile matbu bir metnin ilgili yerlerine 
kullanıcıdan çektiğimiz verileri ekleyebilir, bu sayede 
matbu bir metni herkes kendine göre kişiselleştirebilir.
aşağıda bunun bir örneği bulunmaktadır. format metonun farklı 
şekillerde kullanımı mevcuttur. Aşağıda yer alan ilk örnekte print
fonksiyonuna metod olarak ekledik. Detaylı bilgi için aşağıdaki kodlar incelenebilir.
"""
print(aciklama)
ad = input("Lütfen adınızı giriniz: ")
soyad = input("Lütfen soyadınızı giriniz: ")
yas = input("lütfen yaşınızı giriniz: ")
print("""
merhaba ben {} {}. Ben {} yaşındayım.
Herkese başarılar dilerim.
""".format(ad, soyad, yas))

print("#"*50)
print("""yukarıda yer alan örneğin aynısını format metodu ile farklı bir 
şekilde yapalım. tek yapmamız gereken matbu metni bir değişkene atamak ve 
ve sonrasında değişkenin sonuna format metodunu eklemek""")
matbu_metin = """merhaba ben {} {}. Ben {} yaşındayım.
Herkese başarılar dilerim."""
print("fotmat metodu ikinci yöntem. Valuable.format(a,b,c,...)\n","#"*40)
print(matbu_metin.format(ad, soyad, yas))