# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:22:45 2021

@author: C8381-Tommyhappy    """


left_hand = set("qazwsxedcrfvtgb")
right_hand = set("yhnujmıköolçpşğiü")
word1 = "tester"
word2 = "polly"
word3 = "clarusway"

if word1 in left_hand or right_hand:
    print(False,"uses only left-hand fingers")
else:
    print(True,"uses both hand fingers")

if word2 in left_hand or right_hand:
    print(False,"uses only left-hand fingers")
else:
    print(True,"uses both hand fingers")
    
if word3 in left_hand and right_hand:
    print(False,"uses only left-hand fingers")
else:
    print(True,"uses both hand fingers")