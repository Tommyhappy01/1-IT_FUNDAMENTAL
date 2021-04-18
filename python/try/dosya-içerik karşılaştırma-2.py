dosya_1 = open("isimler_1.txt", encoding = "utf-8")
dosya_1_oku = dosya_1.readlines()
print("Birinci dosyada yer alan isimler: ",*dosya_1_oku, sep = "")
dosya_2 = open("isimler_2.txt", encoding = "utf-8")
dosya_2_oku = dosya_2.readlines()
print("İkinci dosyada yer alan isimler: ", *dosya_2_oku)
print("her iki dosyada ortak olan isimler:")
for i in dosya_1_oku:
    if i in dosya_2_oku:
        print(i)
        
print("her iki dosyada farklı olan isimler:")
for i in dosya_1_oku:
    if i not in dosya_2_oku:
        print(i)