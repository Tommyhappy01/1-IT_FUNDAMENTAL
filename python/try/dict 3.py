# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:39:12 2021

@author: ÖKTEN
"""
"""
family = {"name1":"rana", "name2":"Eda","name3":"ekrem"}
print(family)
family["name4"]="angela"
print(family)

dict_by_dict = dict(animal = "dog", planet = "neptun",
                    number = 40, is_good = True)
print(dict_by_dict)"""

family =dict(name1="rana", name2="Eda")
print(family)

family = {"name1":"rana", "name2":"Eda","name3":"ekrem"}
print(family)
family["name4"]="angela"
print(family)

print(list(family.items()), '\n')

print(list(family.keys()), '\n')

print(list(family.values()))

family.update({"name5": "ela"})            #ekledi
family.update({"name1": "elanurayşe"})     # günelledi
del family["name2"],family["name5"]  #tek satırda family [ ], family [ ]

# del family["name5"]
print(family)
print("name1" in family)
print(family.values())
print("angela" in family)
#◄print("bir" in ["bir",1,7,])

#nesned dictionary



