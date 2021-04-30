# -*- coding: utf-8 -*-
"""
@author: C8381-Tommy 

fibonacci number
    Fn = Fn-1 + Fn-2 
    F0 = 0 and F1 = 1.
 """ 
                      
fib=[]

def fibonacci(n):
    a,b =0,1
    
    while a<=n:
        print(a,end = " ")
        a,b = b,a+b
     
print(fibonacci(55))

def fibonacci(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print("fibonacci: ", end=' ')
        print('0',a,b,end=' ')
        for i in range(n-3):
            toplam = a + b
            b=a
            a= toplam
            print(toplam,end=' ')
        print()
        return b
         
fibonacci(11)