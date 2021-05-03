#!/usr/bin/env python
# coding: utf-8

# <center><img src="https://github.com/aaron-clarusway/fullstack/blob/master/itf-logo.png?raw=true"  alt="alt text" width="200"/></center>
# <br>
# <h1><p style="text-align: center; color:darkblue">Python Basic & Plus</p><h1>
# <center><h1>Workshop - 3</h1></center>
# <p><img align="right"
#   src="https://secure.meetupstatic.com/photos/event/3/1/b/9/600_488352729.jpeg"  width="15px"></p>
# <br>
# 
# 
# # Subject: Collections - Control Flow Statements - Functions

# ## Coding Challenge -1 : Validate Combination of Brackets
# 
# Purpose of the this coding challenge is to solve a combination problem using loops.
# 
# ### Learning Outcomes
# 
# At the end of the this coding challenge, students will be able to;
# 
# - understand the use of loops.
# - solve the advanced and complicated problems.
# - understand the importance of pattern recognition.
# - get a better understanding in manipulating lists or strings.
# 
# ### Problem Statement
#   
# - Write a function that given a string containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determines if the input string is valid or not by using following rules.
# 
# - An input string is valid if:
# 
#   - Open brackets must be closed by the same type of brackets.
# 
#   - Open brackets must be closed in the correct order.
# 
# - Note that an empty string is also considered valid.
# 
# - Example for user inputs and respective outputs
# 
# ```bash
# Input        Output
# --------:    ------:
# "()"         True
# "()[]{}"     True
# "(]"         False
# "([)]"       False
# "{[]}"       True
# ""           True
# ```

# ### Solution :

# In[50]:


def parantez(veri):
    pr={"(":")","{":"}","[":"]"}
    stack = []
    left = [i for i in veri if i in pr.keys()]
    right = [i for i in veri if i in pr.values()]
    if len(left) != len(right) :
        return False
    elif len(veri) == 0:
        return True
    else:
        for i in veri:
            if i in pr:
                stack.append(i)
            else:
                    if i in pr.values():
                        if pr[stack[-1]] == i:
                            stack.pop()
        return not stack
print(parantez("()"))
print(parantez("(]"))
print(parantez("([)]"))
print(parantez("([]){}"))
print(parantez("()[]{}"))
print(parantez(")[]{}"))


# ## Coding Challenge - 2: Calculate Stock Profit
# 
# The purpose of this coding challenge is to write a program that calculates maximum profit you could get from a stock.
# 
# ### Learning Outcomes
# 
# At the end of this coding challenge, students will be able to;
# 
# - analyze a problem, identify, and apply programming knowledge for appropriate solution.
# 
# - design, implement `arithmetic operators` effectively in Python to solve the given problem.
# 
# - demonstrate their knowledge of algorithmic design principles by solving the problem effectively.
# 
# ### Problem Statement
# 
# Given an array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. Note that you must buy before you can sell it.
# 
# For example, given ``[9, 11, 8, 5, 7, 10]``, you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
# 
# Example of different list of stock prices and respective outputs.
# 
# ```bash
# List = [75,73,60,100,120,130]
# Output = 70
# List = [10,20,23,22,17,30]
# Output = 20
# List = [1,6,19,59,30,60]
# Output = 59
# ```

# ### Solution-1 :

# In[61]:


def buy_and_sell(kar):
    buy = min(kar)
    sell = max(kar[kar.index(buy):])
    return sell-buy


# In[47]:


buy_and_sell([1,45,6,90,10])


# In[ ]:





# In[53]:


buy_and_sell([22,33,44,55,66])


# In[ ]:





# ### Solution-2 :

# In[60]:


def buy_and_sell(liste):
    sonuç = []
    for i in range(len(liste)):
        sonuç.append(max(liste[i:]) - liste[i])
    return(max(sonuç))
buy_and_sell([10,52,10,250,35,40,100,55])


# ## Coding Challenge - 3: Morse Translator
# 
# The purpose of this coding challenge is to write a program that translates the plain text to morse code.
# 
# ### Learning Outcomes
# 
# At the end of this coding challenge, students will be able to;
# 
# - Analyze a problem, identify, and apply programming knowledge for an appropriate solution.
# 
# - Implement loops to solve a problem.
# 
# - Make use of dictionary data structure to map values. 
# 
# - Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.
# 
# ### Problem Statement
# 
# Write a function that takes in a plain text as input and converts it into morse alphabet. Following alphabet can be used:
# 
# ```bash
# {
#   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#   'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#   '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#   ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#   '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
# }
# ```
# - Expected Outputs:
# 
# ```bash
# Input: Hello world!
# 
# Output:
# .... . .-.. .-.. ---   .-- --- .-. .-.. -.. -.-.--
# 
# Input: Good job!
# 
# Output: --. --- --- -..   .--- --- -... -.-.--
# ```

# ### Solution :

# In[62]:


mors = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

def encode_morse(a):
    a= a.upper()
    for i in a:
        print(mors[i], end= " ")
encode_morse(a="clarusway")


# In[ ]:





# In[52]:


a = {1:"a",2:"b",3:"c"}
key =list(a.keys())
value= list(a.values())
value


# In[ ]:





# assigment_1

# In[63]:


def num_total(a,b):
    if a==b:
        return (a+b)*2
    else:
        return a+b 


# In[64]:


num_total(20,20)


# In[ ]:


assigment_6


# In[3]:


def prime_num(num):
    for i in range(num):
        for j in range(i):
            if i%j ==0:
                print(i, "Asal sayıdır", end=" ")
            else:
                print("Asal sayı değildir.")


# In[ ]:


prime_num(2)


# In[ ]:


sayi1 = int(input("Sayı 1: "))
sayi2 = int(input("Sayı 2: "))
 
print(sayi1,"ile",sayi2,"arasındaki asal sayılar:")
 
for sayi in range(sayi1,sayi2 + 1):
   if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               break
       else:
           print(sayi)


# In[1]:


sayi1 = int(input("Sayı 1: "))
sayi2 = int(input("Sayı 2: "))
 
print(sayi1,"ile",sayi2,"arasındaki asal sayılar:")
 
for sayi in range(sayi1,sayi2 + 1):
   if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               break
       else:
           print(sayi, end = " ")


# In[ ]:





# In[ ]:





# In[ ]:




