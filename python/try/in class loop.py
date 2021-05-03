#!/usr/bin/env python
# coding: utf-8

# In[123]:


text = ["one","two","three"]
number=[1,2,3]
city=["tokyo","kiev","istanbul"]
print(zip(text,number))
#list(zip(text,number))
print(* zip(text,number))
print(zip(text,number))


# In[117]:


evens=[]
odds=[]
for i in range(10):
    if i%2==0:
        evens.append(i)
    else:
        odds.append(i)
print(evens)
print(odds)


# In[119]:


numbers=[1,2,6,8,9,10,11,20,30,15]
even=0
odd=0
for i in numbers:
    if not i%2:
        even += 1
    else:
        odd += 1
print("the count of even numbers",even)
print("the count of odd numbers",odd)


# In[120]:


if 1:
    print("çalış")


# In[121]:


if 0:
    print("çalışmadı") # baody inemedei


# In[26]:


0%2


# In[27]:


11%2


# In[29]:


not 1


# In[30]:


not 0


# In[129]:


for i in range(1,10):
    print(str(i)*i)


# In[127]:


"2"*2


# In[42]:


"1"*3


# In[131]:


total=0
for i in range(1,76):
    total+=i
total


# In[55]:


names = ["susan", "tom", "edward"] 
mood = ["happy", "sad"]
for i in names:
    for ii in mood:
        print(i+ii)
    


# ### list comprehenson'ların temel yapısı:

# In[61]:


my_list = [1,2,3,4,5,6]
new_list = []
for i in my_list:
    if i% 2 :
        new_list.append(i**2)
new_list


# (expression for item in iterable]
# 
# for item in iterable:
#         expression        #expression başa giderse tek satıra  iner.
#                            virgülle ayırıp listeye ekleme yapar

# In[133]:


[i for i in range(5)]


# In[135]:


listem = []
for i in range (5):
    listem.append(i)
listem


# In[136]:


[i for i in range(5)]


# In[137]:


listem = []
for i in range (5):
    listem.append(i**2)
listem


# In[69]:


[i**2 for i in range(5)] # en başta body sonra for condition


# In[75]:


[a**2 for a in range(15)] # aynı satırda kareleri al listele


# In[149]:


[i%2 for i in range(20)]


# In[145]:


[i//2 for i in range(20)]


# In[80]:


### turnerı condition


# In[81]:


condition = True
if condition :
    a = 1
else:
    a=0
print(a)


# In[82]:


a=1 if 2<4 else 0
print(a)


# In[83]:


a=1 if 5<4 else 0
print(a)


# In[84]:


print(1 if 2<4 else 0)


# ###  ternary "if" condition yapısı
# execute-body1     if condition     else execute-body2
#    
#    if body                           else body
# 
# sadece if   else yapısını öğrendik

# In[ ]:


my_list = [1,2,3,4,5,6]


# In[86]:


[i**2 for i in my_list if i%2]


# In[87]:


[i**2 for i in my_list if not i%2]


# In[150]:


a =[i for i in my_list if not i%2]
a 


# In[151]:


b = (i**2 for i in my_list)
b  #tuple olduğundan sakladı


# In[96]:


print(*b)


# In[152]:


for i in b:
    print(i)
    print(i, end ="")


# In[153]:


a = (i**2 for i in my_list)
print(next(a))    # teke tek iterate eder


# In[154]:


print(next(a))  #ikinci elemanı serbest kaldı


# In[155]:


print(next(a)) #3. elemanı serbest kaldı


# In[156]:


print(next(a))  #4. elemanı serbest kaldı


# In[157]:


print(next(a)) 


# In[158]:


print(next(a)) 


# In[159]:


print(next(a)) 


# In[ ]:





# In[ ]:



