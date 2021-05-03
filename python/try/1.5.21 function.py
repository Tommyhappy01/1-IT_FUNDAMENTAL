#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculator(a, b, opr) :
    if opr == '+' :
        return(a + b)
    elif opr == '-' :
        return(a - b)
    elif opr == '*' :
        return(a * b)
    elif opr == '/' :
        return(a / b)
    else :
        return('Only 4 math operations')
a = int(input("please enter a number"))
opr = str(input("please enter math operation"))
b = int(input("please enter a number"))
print(calculator(a, b, opr))


# In[ ]:





# In[15]:


def filtervowels(letter):
    vowels = ["a","e","i","o","u"]
    if  letter.lower() in vowels:
        return True
    else:
        return False


# In[16]:


filtervowels("b")


# In[ ]:





# In[5]:


vowels = ["a","e","i","o","u"]


# In[17]:


"b" in vowels


# In[18]:


sentence= "the clarusway is the best"


# In[20]:


filtered_vowels = filter(filtervowels, sentence) # baştan başlar sona kadar fonksiyonu uygular


# In[21]:


print(*filtered_vowels)


# In[ ]:


### sessizleri yapınız


# In[33]:


def absolute_value(number):
    """ This function returns the absolute value of the entered number"""
    if number > 0 :
        return number
    else:
        return - number


# In[35]:


absolute_value(-2)


# In[32]:


print(absolute_value.__doc__)


# In[38]:


abs.__doc__


# In[40]:


def pos(a,b):
    print(a, "ilk argüman")
    print(b, "ikinci argüman")
pos(10,36)                        # sıra önemli


# In[41]:


pos("beş","on")                   # sıra önemli


# In[42]:


pos(["beş","on"],{2,44})         # sıra önemli


# In[61]:


a="i"
b="love"
c= "you"
def texter(c,a,b):
    return(a,b,c)


# In[58]:


texter(c,a,b)


# In[63]:


texter(a,b,c)


# In[66]:



a="i"
b="love"
c= "you"
def texter1(x,y,z):
    return(f"{a} {b} {c}")


# In[67]:


texter1(a,b,c)


# In[68]:


def concat(a,b):
    print(a+b)


# In[69]:


concat(a= "istanbul ",b="erzurum")


# In[73]:


concat(b="erzurum ",a= "istanbul")


# In[74]:


concat(b="Seoul ",a= "London ")


# In[75]:


concat("erzurum", "istanbul")          # possional olarakta atandı


# In[78]:


def texter(text1,text2,text3):
    print(text1="you",text2="i",text3="love")


# In[80]:


texter(text1,text2,text3)


# In[81]:


def func(x= "ali", y= 11):               # keyword arg tanımlama = ile keyword 
    body                                 # parametre tanımlıyoruz.
    


# In[87]:


def default(a= "ali", b= 33):
    print(a, "is",b, "years old.")


# In[88]:


default()                               # değer deult olduğundna boş bile gönd alır.


# In[89]:


default("mehmet",44)                   # possioanal çağırdım


# In[90]:


default("selvi")                      # tek possional yazdım defaultı kendi getirdi çağırdım


# In[91]:


default(b= "55") 


# In[92]:


default(b= "55", a= "songül") 


# In[94]:


def default(x, a= "ali", b= 33):
    print(a, "and",x,"is",b, "years old.")


# In[95]:


default()


# In[96]:


default("gonca")


# In[111]:


def parrot(voltage, state='a stiff', action='woom', typed='Norweigen Blue'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", typed)
        print("-- It's", state, "!")


# In[97]:


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments 
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# In[112]:


parrot(1000)


# In[113]:


parrot(voltage=1000)                   #possional olmasına rağmen keyword olarak çağırdık


# In[114]:


parrot(voltage=1000000, action='VOOOOOM')   #keyworde yeni değer atanabilir


# In[116]:


parrot(voltage=100000000000,action=" mmooommmm")     #keyword kullanılırsa sıra önemli değil


# In[117]:


parrot(action=" mmooommmm",voltage=100000000000)  #keyword kullanılırsa sıra önemli değil


# In[118]:


parrot('a million', 'bereft of life', 'jump')         # solda sağ sırayla atar


# In[119]:


parrot('a thousand', state='pushing up the daisies') 


# In[ ]:





# In[120]:


def parrot( state='a stiff',voltage, action='woom', typed='Norweigen Blue'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", typed)
        print("-- It's", state, "!")
                  # possional yer değişti hata verdi
                  # non-default argument follows default argument


# In[121]:


def argu(a,b="dünya",c,d ="satürn") :
    print(a,b,c,d, sep= "\n")
                   # possional yer değişti hata verdi
                   # possional bitene kadar başa yazılır.
    


# In[122]:


def argu(a,c, b="dünya", d ="satürn") :
    print(a,b,c,d, sep= "\n")
                   # possional yer değişti hata verdi
                   # possional bitene kadar başa yazılır.


# In[123]:


argu()             # a ve c ye değer ata diyor
                   # b ve d  default


# In[124]:


argu("üranüs","jupiter")  # a ve c ye değer atadık defaultlar geldi


# In[127]:


argu(d= "güneş", a= "dünya",c= "mars",e="sun")
                                    # argu() got an unexpected keyword 
                                    # argument 'e'. Yani bilinmeyen arg var 


# In[128]:


argu(d= "güneş", a= "dünya",c= "mars",b="sun")


# In[129]:


argu(a= "dünya", c = "merkür")   #possional doldu


# In[130]:


argu("üranüs",a= "dünya", c = "merkür") # en baştaki arg a ya üranüs atadık.
                                        # 2 tane almaz a


# In[ ]:


# pass satırı geçmek  için kullanılır. Bir sonraki satıra geçer.


# In[131]:


pass


# In[133]:


if 10>0:
    pass
    print("ben ikinci satırım")


# ### arbitrary  belirsiz sayıda arguman bir belirsizlik var.  -----* yıldız asteriks -----  koyulacak

# In[134]:


def city(capital, continent='Europe'):
    print(capital, 'in', continent)
city('Athens')                                 # we don't have to pass any arguments into 'continent'
city('Ulaanbaatar', continent='Asia')          # we can change the default value by kwargs
city('Cape Town', 'Africa')                   # we can change the default value by positional args.


# In[142]:


def fruiterer(fruit1,fruit2):
     print("I want to get", fruit1, fruit2)
    
fruiterer("orange","banana")


# In[143]:


def fruiterer(*fruit) :
    print("I want to get :")
    for i in fruit :
        print('-', i)
fruiterer('orange', 'banana', ['melon', 'ananas'])


# In[164]:


def slicer(*num):
    odd_list=[]
    even_list=[]
    for i in num:
        if num %2 ==0:
        even_list.append(i)
    else:
        odd_list.append(i)
    print("even_list:",even_list)
    print("odd_list:",odd_list)


# In[144]:


slicer(1,2,3,4,5,6,7,8,9)


# In[159]:


def slicer(*num):
    print("evens:", [i for i in num if i%2==0])        # önemliiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
    print("odd:",[i for i in num if not i%2==0])       # önemliiiiiiiiiiiiiiiiiiiiiiiiiiiiiii


# In[160]:


slicer(1,2,3,4,5,6,7,8,9)             # önemliiiiiiiiiiiiiiiiiiiiiiiiiiiiiii


# ###  ** kwargs    dictionary de kullanacağız  iterable dict muamelesi yaptık.

# In[166]:


sözlük = dict(ahmet= "bacanak", mehmet = "ağabey", meryem= "anne")


# In[167]:


sözlük


# In[172]:


def sözlük(**a):
    for key,value in a.items():
        print(key,value)         # key word arg kabul eder


# In[174]:


sözlük(ahmet= "bancanak", mehmet = "baldız", meryem = "anne")


# In[175]:


sözlük(ahmet= "bancanak", mehmet = "baldız", meryem = "anne",leyla = "komşu", zeyno= "bebek")


# In[176]:


def animals(**kwargs):
    for key, value in kwargs.items():
        print(value, "are", key)
animals(Carnivores="Lions", Omnivores="Bears", Herbivores="Deers", Nomnivores="Human")


# In[192]:


def organizer(**kwargs):
    list1=[]
    list2=[]
    for key,value in kwargs.items():
        list1.append(key)
        list2.append(value)
    print(list1,list2, sep= "\n")        


# In[193]:


organizer(beth=26, oscar = 42, justin= 18, frank= 33)


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




