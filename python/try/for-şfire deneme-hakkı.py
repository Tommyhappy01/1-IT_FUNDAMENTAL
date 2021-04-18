# kullanıcıya 3 deneme hakkı verme

şifre = "123456"

for i in range(0,3):
    password = input("Lütfen şifreiniz giriniz")
    if password == şifre:
        print("sisteme hoşgeldiniz")
        break
    elif i == 2:
        print("şifre deneme hakkınız doldu")
        break
    else:
        print("şifrenizi yanlış girdiniz. Tekrar deneyiniz")
    i += 1