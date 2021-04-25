#!/usr/bin/env python
# coding: utf-8

# ### FUNCTİONS WORK
# Fonksiyonların görevi, karmaşık işlemleri bir araya toplayarak, bu işlemleri tek adımda yapmamızı sağlamaktır. Fonksiyonlar çoğu zaman, yapmak istediğimiz işlemler için bir şablon vazifesi görür. Fonksiyonları kullanarak, bir veya birkaç adımdan oluşan işlemleri tek bir isim altında toplayabiliriz. Python’daki ‘fonksiyon’ kavramı başka programlama dillerinde ‘rutin’ veya ‘prosedür’ olarak adlandırılır. Gerçekten de fonksiyonlar rutin olarak tekrar edilen görevleri veya prosedürleri tek bir ad/çatı altında toplayan araçlardır.

# In[8]:


print('Say: I love you!')
print()


# In[6]:


a = 3
b = 5
multiply(3,5)


# In[10]:


def my_function():
  print("Hello from a function")
my_function()


# In[32]:


def my_function(fname):        # fname burda parametre
    print(fname+" happy")
my_function("erol")
my_function("kenan")
my_function("ejder")


# In[34]:


def my_function(fname,lname):
    print(fname + "     "+ lname)
my_function("emil","refsnes")


# In[35]:


def my_function(*kids):
    print("the youngest child is  " + kids[2] )
my_function("ali","veli","asım")


# In[36]:


def my_function(child3, child2, child1):
  print("The youngest chld is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# In[37]:


def o_function(**kid):
  print("his last name is " + kid["lname"])

o_function(fname = "Tommy", lname = "kibar")


# In[38]:


bazıları booliçindeki koşullu algoritmaya göre tür döndürür . Örneğin; , ve .all(iterable)any(iterable)callable(object)
Bazıları veri türlerini birbirine dönüştürmenize yardımcı olur. Örneğin; bool(), float(), int()Ve str().
Bazıları koleksiyon türlerini oluşturmanıza ve işlemenize izin verir. Mesela: dict(), list(), tuple(), set(), len(), frozenset(), zip(), , ve .filter(function, iterable)enumerate(iterable)
Bazıları sayılarla uğraşır. Mesela: max(), min(), sum()ve round().
Diğerleri özel amaçlar için inşa edilmiştir. Bazı karmaşık uygulamalar yaparlar. Örneğin: , , , , , , ve .map(function, iterable, ...)eval(expression[, globals[, locals]])sorted(iterable)open()dir([object])hash()help([object])


# In[33]:


def function_name(arguments) :
    execution bod


# In[36]:


def ilk(argument_1,argument_2):
    print(argument_1**2 + argument_2**2)
ilk(6,3) #değerler (6 ve 3), parantez içinde işlev çağrısında 
         #sağlanan argümanlara tahsis edilmiştir.


# In[39]:


ilk(19,11) #Girinti olmadığında, işlevin tanımlanma sürecinin 
            #sona ermesi gerektiği anlamına gelir .


# In[39]:


#yukarıda değerler (6 ve 3), parantez içinde işlev çağrısında 
#sağlanan argümanlara tahsis edilmiştir.


# In[5]:


def multiply(a,b):
    print(a*b)
multiply(3,5)
multiply(-1,2.5)
multiply(" çok iyi",3)


# In[6]:


def a(a,b):
    print(a*b)
a(3,5)
a(-1,2.5)
a(" çok iyi",3)


# In[9]:


def motto():
    print("don't hesitate to reinvent yourself" )
motto()


# In[12]:


def fib(n):
        a,b = 0,1
        while a< n:
            print(a,end=" ")
            a,b = b,a+b
fib(100)


# In[21]:


def ç_1(a,b):
    print(a*b)  #it prints something
ç_1(10,5)


# In[19]:


print(ç_1(2,3))
print(ç_2(6,5))


# In[22]:


def ç(a,b):
    return a*b
print(ç(10,5)) #returns any numeric data type value


# In[31]:


a = print("merhaba")
print(a)


# In[28]:


b= "ali"
print(b)
print("a")


# ###  returnBir işlevde birden fazla anahtar sözcük varsa , o işlevin çalıştırılmasının ilkinden sonra sona ereceğini unutmayın.

# In[5]:


def kayıt_oluştur(isim, soyisim, işsis, şehir):
    print("-"*30)

    print("isim           : ", isim)
    print("soyisim        : ", soyisim)
    print("işletim sistemi: ", işsis)
    print("şehir          : ", şehir)

    print("-"*30)

kayıt_oluştur("Fırat", "Özgül", "Ubuntu", "İstanbul")
kayıt_oluştur("Mehmet", "Öztaban", "Debian", "Ankara")


# ### function definiation and function call 
# builtin functions ve custom functions

# In[45]:


def selamla():
    print("Elveda Zalim Dünya!")
selamla()


# In[46]:


def sistem_bilgisi_göster():
    import sys
    print("\nSistemde kurulu Python'ın;")
    print("\tana sürüm numarası:", sys.version_info.major)
    print("\talt sürüm numarası:", sys.version_info.minor)
    print("\tminik sürüm numarası:", sys.version_info.micro)

    print("\nKullanılan işletim sisteminin;")
    print("\tadı:", sys.platform)

sistem_bilgisi_göster()


# In[48]:


sayı = 12
çıktı = "{} sayısının karesi {} sayısıdır"
print(çıktı.format(sayı,sayı**2))


# In[8]:


def kare_bul():
    sayı=15
    çıktı="{} sayısının karesi {} sayısıdır"
    print(çıktı.format(sayı,sayı**2))
kare_bul()


# In[20]:


def longer(a, b):
    if longer(a) > longer(b):
        longer= a
    else:
        longer=b
    print(longer)
longer("Richart","John")


# In[17]:


def who(first, last) :  # 'first' and 'last' are the parameters(or variables)
    print('Your first name is :', first)
    print('Your last name is :', last)
    
who('Guido', 'van Rossum')  # 'Guido' and 'van Rossum' are the arguments


# In[5]:


def who(first, last) :  # 'first' and 'last' are the parameters(or variables)
    print('Your first name is :', first)
    print('Your last name is :', last)

print()
who('Marry', 'Bold')  # 'Marry' and 'Bold' are also the arguments


# In[6]:


def pos_args(a, b):
    print(a, 'is the first argument')
    print(b, 'is the second argument')

pos_args(3,4)
print()
pos_args(4,3)


# In[7]:


pos_args('first','second')
print()
pos_args('second', 'first')


# In[8]:


def who(first, last) :  # same structure as the previous one
    print('Your first name is :', first)
    print('Your last name is :', last)

who(first='Guido', last='van Rossum')  # calling the function is different
# we used kwargs to pass the values into the function


# In[11]:


def who(first, last) :  # same structure as the previous one
    print('Your first name is :', first)
    print('Your last name is :', last)

who("Guido","van Rossum")


# In[13]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments 
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# ### built in function...

# In[21]:


# abs mutlak değer dönderir. int,float,complex


# In[33]:


sayı = abs(-29)
sayı


# In[31]:


sayı1 = abs(24.02)
sayı1


# In[34]:


sayı2 = abs(44+5j)
sayı2


# In[ ]:


# all tüm öğelerin True olup olmadığını kontrol etmek kullanılır.


# In[35]:


liste =[True,True,True]
a= all(liste)
a


# In[37]:


liste =[True,False,True]
a= all(liste)
a


# In[40]:


liste =[10,-10,44,11.03,True,True]
a= all(liste)
a


# In[43]:


liste =[0,15,32,41,16.25]         # 0 falsy değer dönderdi
a= all(liste)
a


# In[48]:


# any ise "herhangi birinin" True olduğunu kontrol eder.


# In[47]:


liste =[False,"Bir",True,True,True]   # bir tane True yetti.
a= any(liste)
a


# In[49]:


liste =[False,"Merhaba",1,6]         # str ifade de olabilir.
a= any(liste)
a


# In[52]:


liste = []                           # Boş liste False dönderir.
a = any(liste)
a


# In[ ]:


# bool fonksiyonu boolen değerini verir. Ya False ya da True


# In[53]:


a = bool(55)                          # int değer True oldu
a 


# In[54]:


a = bool(True)                        # True 
a


# In[57]:


a = bool("Clarusway")                  # str değer True dönderdi. 
a


# In[59]:


a = bool(False)                        # False  Falsy değer dönderdi.
a


# In[60]:


a = bool()                             # Boş nesne False değer dönderdi.
a


# In[62]:


a = bool([])                           # Boş nesne False değer dönderdi.
a


# In[64]:


a= bool(0)                              # 0 da False değer dönderir.
a


# In[65]:


# callable ile belirtilen nesne  çağıralabilir ise "True" aksi takdirde "False" dönderir.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




