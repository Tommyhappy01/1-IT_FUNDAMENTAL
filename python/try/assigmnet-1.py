# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 19:59:22 2021

@author: Elif & Zeynep
"""


deposited_money = 1000  # yatırılan para miktarı
profit_rate = 0.07  # günlük kâr oranı
for i in range(0,7):  #  haftanın 7 günü için aynı işlemleri tekrarla
    deposited_money += profit_rate * deposited_money  # elde edilen kârı ana paraya ekle
print(round(deposited_money,2))  # 7 günün sonunda elde edilen toplam para

para = 1000
profit = 0.07*1000
para += profit
print(para)
