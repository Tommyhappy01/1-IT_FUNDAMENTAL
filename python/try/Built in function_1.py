#!/usr/bin/env python
# coding: utf-8

# ### FUNCTİONS WORK
# Fonksiyonların görevi, karmaşık işlemleri bir araya toplayarak, bu işlemleri tek adımda yapmamızı sağlamaktır. Fonksiyonlar çoğu zaman, yapmak istediğimiz işlemler için bir şablon vazifesi görür. Fonksiyonları kullanarak, bir veya birkaç adımdan oluşan işlemleri tek bir isim altında toplayabiliriz. Python’daki ‘fonksiyon’ kavramı başka programlama dillerinde ‘rutin’ veya ‘prosedür’ olarak adlandırılır. Gerçekten de fonksiyonlar rutin olarak tekrar edilen görevleri veya prosedürleri tek bir ad/çatı altında toplayan araçlardır.

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


# callable() ile belirtilen nesne  çağıralabilir ise "True" aksi takdirde "False" dönderir.


# In[1]:


def fonksiyon():
    Clarusway= "En iyi kurs"            # tanımladığımız fonkiyon çağırıldı.
callable(fonksiyon)


# In[ ]:


def fonksiyon():
    Clarusway= "En iyi kurs"            # Normal değişken çağıralamaz.
callable(Clarusway)


# In[ ]:


# divmod() ile verilen değerlerin bölüm ve kalan argümanlarının bir tuple"ını döndürür.


# In[5]:


a = divmod(10,2)                       #10/2 işleminde bölüm = 5, kalan =0 
a


# In[15]:


a = divmod(32,3)                       #32/3 işleminde bölüm = 10, kalan =2 
a


# In[16]:


a = divmod(-32,3)                       #-32/3 işleminde bölüm = 11, kalan =1 
a                                       # yaptı, 33 e göre davrandı ( önemli...)


# In[17]:


a = divmod(12.5,3)                       #12.5/3 işleminde bölüm = 4.00, kalan =0.5 
a


# In[ ]:


# isinstance()ile  belirtilen nesne beirtilen tipte ise True döner aksi halde False.


# In[19]:


a = isinstance(125, int)                       #125 integer (nesne ve sınıf bilgisi) 
a


# In[20]:


a = isinstance(125.0, float)                    #125.0 float (nesne ve sınıf bilgisi) 
a


# In[21]:


a = isinstance(125.0, str)                       #125.0 str mi? (nesne ve sınıf bilgisi) 
a


# In[22]:


a = isinstance("Clarusway", str)                  #Clarusway str mi? (nesne ve sınıf bilgisi) 
a


# In[23]:


a = isinstance("Clarusway", (str,int,float,dict,tuple,list,set))
a                                                 #Clarusway str,int,vb. diye de bakılabilir. 


# In[ ]:


a = isinstance("Clarusway", (int,float,dict,tuple,list,set))
a                                                #Clarusway int,list,vb. diye de bakıldı, str 
                                                 #sormazsak  False döndürür.


# In[ ]:


# max() ile  en yüksek değere sahip öğeyi dönderir.


# In[25]:


a = max(1, 2 , 147, 3.5, 9, 1453, 10, 39, 1001)    # En büyük değer 1453 float ta dahil. 
a


# In[28]:


a = max("a","z","G","t","L","elma","r","zeplin","w")# str ifade de alfabetik sonuç dönderir.
a


# In[33]:


a = max("a","z","G","t","L","m","r","w")           # str ifade de alfabetik sonuç dönderir.
a


# In[36]:


a = max("a","z","G","ü","t","L","m","r","w")       # tr karekterlerinde ascii koda göre dönderir.
                                                   # z=90 ü=129
a


# In[44]:


a = max("Clarusway", "8", "kurs","başarı")         # str ifade de alfabetik sonuç dönderir.
a


# In[ ]:


a = max("Clarusway", "8", "kurs","başarı")         # int ve str ifade olursa erro verir.
a


# In[ ]:


# pow() ile  üslü saılarla heasplama yaparken kullanılır.


# In[45]:


a = pow(5,4)                                      #5'in 4. kuvveti 
a


# In[107]:


a = pow(5,4,5)                                    #5'in 4. kuvvetinin %5 
a


# In[ ]:


# round() ile ondalık sayıyı tamsayı veya yakın ondalığa yuvarlar.


# In[50]:


a = round(5.55)                                    # .5 üstünde olduğu için yukarı yuvarladı. 
a


# In[53]:


a = round(3.145736542,3)                          # kaç ondalık olmasını istiyorsak belirttik.
a


# In[56]:


a = round(-56.1542,2)                            # - değerde de olabilir.
a


# In[57]:


a = round(3.1457342)                            # ondalık kısmı belirtmedik tam sayı yaptı
a


# In[77]:


a = round(-12.37)                              # ondalık kısmı belirtmedik tam sayı yaptı
a


# In[79]:


a = round(36/5)                                # işlemi yapıp yuvarladı
a


# In[80]:


a = round(36/5,1)                              # işlemi yapıp 1 ondalıkla yazdı
a


# In[78]:


# sorted() ile belirtilen nesnelerin sıralı bir listesini verir.


# In[63]:


liste = ("a","z","G","t","L","m","r","w")           # sıralamada önce büyük harf sonra küçük harf
a = sorted(liste)
a


# In[64]:


liste = (3,6,9,10,11,55,33,44,56,101,24)           # küçükten büyüğe doğru
a = sorted(liste)
a


# In[66]:


liste = (3,6,"iki","bir","onaltı",10,11,55)       # int ve str olursa error verir.
a = sorted(liste)
a


# In[68]:


liste = ("b","c","d","d","D","e","t","p","y","z","j",)       # int ve str olursa error verir.
a = sorted(liste)
a


# In[69]:


liste = ("b","c","d","d","D","e","t","p","y","z","j",)       # int ve str olursa error verir.
a = sorted(liste,reverse=True)                               # reverse değeri True olursa tersten sıralar.
a


# In[ ]:


# sum() bir sayıyı veya yenilenebilir tüm öğelerin toplamını dönderir.


# In[70]:


liste = (3,6,9,10,11,55,33,44,56,101,24)                 # alayını topladı.
a = sum(liste)
a


# In[72]:


liste = (3,-6,9,-10,-11,-55,33,-44,56,-101,24)           # eksi değerleride dikkate alır ve toplar.
a = sum(liste)
a


# In[75]:


liste = (3,-6,9,-10,24,36)                              # ilave de edebilirde.
a = sum(liste,1000)
a


# In[ ]:


# ascii() bir nesnenin ekrana basılabilir halini verir.ascii kodunu verir


# In[81]:


liste = ("clarusway")                              # çıktıyı str verdi.
a = ascii(liste)
a


# In[86]:


liste = ("\n")                                     # normalde kaçış dizisi görevini yapmasını sağlamak
                                                   # yerine u kaçış dizisinin ekrana basılabilri 
                                                   # halini verir.
a = ascii(liste)
a


# In[88]:


liste = ("çekiç")                                  # Türkçe karekterlerinde UNİCODE temsilini dönderir.
a = ascii(liste)
a


# In[94]:


for i in liste:                                    # Türkçe karekterlerinde UNİCODE temsilini dönderir.
    print(ascii(i))


# In[96]:


liste = ("çekiç","erik","armut","ada")             # liste olma özelliğini yitirip bir karakter 
a = ascii(liste)                                   # dizisi haline gelir.
a


# In[ ]:


# repr() ascii koda çok benzer, ascii olmayan karekterlere davranışlar açısından 
#birbirinden ayrılır.


# In[98]:


ascii('şoför')


# In[99]:


repr('şoför')


# In[ ]:


# bin() ikili say düzenindeki karşılığını verir. karekter dizisi verir.


# In[102]:


bin(102)
bin(2)


# In[ ]:


# bytes() bytes türünde nesneler oluşturur.list(), str(), int(), set(), dict() gibi fonksiyonlara 
#çok benzer.Farklı veri tiplerini‘bayt’ adlı veri tipine dönüştürür.


# In[103]:


bytes(10)                                     # her birinin değeri 0 olan 10 baytlık veri dönderir.


# In[106]:


bytes(1)                                      # bytes(10) komutuyla oluşturduğumuz a değişkeni içinde
                                              # toplam 10 adet bayt var ve bu baytların her birinin
                                              # değeri 0.


# In[ ]:




