print(""" Hesap Makinesi Uygulaması
eval() fonksiyonu ile uygulama yapma
""")
print(*"-"*20, sep = "~")
print("""
Hesap Makinesi Programına Hoş Geldiniz!
# Toplama işlemi için +
# Çıkarma işlemi için -
# Çarpma işlemi için  *
# Bölme işlemi için   /
operatörlerini kullanınız. Örneğin; iki sayıyı 
çarpmak için: 8*7 şeklinde
bölmek için : 8/7 şeklinde
çıkarma için : 8-7 şeklinde yazınız.

""")
veri = input("lütfen yapmak istediğiniz işlemi giriniz: ")
islem = eval(veri)
print (veri, "işleminin sonucu =", islem)
input()
