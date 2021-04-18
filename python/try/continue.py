while True:
    s = input("Bir sayı girin: ")
    if s == "iptal":
        break

    if len(s) <= 3:
        continue  # döngü başa döner. Sonraki kodlar çalışmaz

    print("En fazla üç haneli bir sayı girebilirsiniz.")