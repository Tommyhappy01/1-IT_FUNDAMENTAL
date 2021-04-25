#samanlıkta iğne arayalım mı;

samanlık = ["yumurta","inek","saman","tezek","tırmık","iğne","yaba"]

print(f" iğne {samanlık.index('iğne')} numaralı indexte")


#tuple kullanarak çoklu değer assing etmek,

v = ("five",5,True)
(x,y,z) = v
print(x,y,z)

#tuple kullanarak çoklu değer assing etmek,

v = ("five",5,True)
(x,y,z) = v
print(x,y,z)


(monday,tuesday,wednesay,thursday,friday,saturday,sunday)= tuple(range(1,8))
print(monday)             #for döngüsü, collections,* ile


print([1,2,3,4]+["onbir","yirmi iki",33]) # 2 liste birleşti

tt = (1,2,[1,3,5])  
print(tt)

tt = (1,2,[1,3,5])
tt[2].append(4)     

x,y =  (10,25)
print(x,y)

#a, b = (10,20,30,40)
a, _, b, _ = (10,20,30,40) #alt tire olursa jenerik atama yaptık
print(a,b)

# hata aldık x,y,z = (11,22,33,44,55)
print(x,y,z)

x,y, *z = (11,22,33,44,55,66)
print(x,y,z)
print(x)
print(z)


x,y, *_ = (11,22,33,44,55,66)
print(x,y)
print(*_)

x, y, *z, t = (11,22,33,44,55,66,77)
print(t) #en sondakini aldı
print(z) #ardakileri aldı z

x, y, *z, t,w = (11,22,33,44,55,66,77,88)
print(t) #en sondakinde bir öncekiydi akılı adamsın python.
print(w) # en sondu zaten 88 oldu.

         