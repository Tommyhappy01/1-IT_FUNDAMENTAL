# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:58:02 2021

@author: ÖKTEN
"""
"""
Step 1:Get input from the user

Step 2:Check if the input number is greater than 1 or not

Step 3:If yes, iterate from the value 2 to the given input value using 'for' loop

Step 4:Check if the value is divisible by 1 and itself.

Step 5:If yes, print "Prime Number"

Step 6:Else, print "Not a Prime Number"

Step 7:Else, print "Enter a positive number"

Step 8:End """

#Python Program to check if the given number is prime or not using function
def finding_prime(Number):
  count = 0 
  for i in range(2, Number):
    if(Number % i == 0):
      count = count + 1 
      return count

n = int(input("Enter the Number: "))
res = finding_prime(n)
if(res == 0 and n != 1):
  print("Prime Number")
else:
  print("Not a Prime Number")