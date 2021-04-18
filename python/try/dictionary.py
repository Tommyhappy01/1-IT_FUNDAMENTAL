# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:54:58 2021

@author: ÖKTEN
"""

a= {}
print(a)
print(type(a))

my_dict = {"marka": "mercedes",
           "renk":"black",
           "year":"2021",
           "sunroof":"Big" }
print(my_dict)
print(my_dict["marka"])       # markaya ulaştık mercedesssss
my_dict["glass color"] = "blue" #ekledik
print(my_dict)

mix_values = {'animal': ('dog', 'cat'),  # tuple type
              'planet': ['Neptun', 'Saturn', 'Jupiter'],  # list type
              'number': 40,  # int type
              'pi': 3.14,  # float type
              'is_good': True}  # bool type
print(mix_values)

mix_keys = {22 : "integer",
            1.2 : "float",
            True : "boolean",
            "key" : "string"}
print(mix_keys)

dict_by_dict = dict(animal='dog', planet='neptun', number=40, pi=3.14, is_good=True)

print(dict_by_dict) #Bir sözlük oluşturmak keys için dict()işlevi kullanırken tırnak işareti kullanmayın .
                    #keys Bir sözlük oluşturmak için yinelemeleri kullanamazsınız 

dict_by_dict = {'animal': 'dog',
                'planet': 'neptun',
                'number': 40,
                'pi': 3.14,
                'is_good': True}

print(dict_by_dict.items(), '\n')
print(type(dict_by_dict.items))
print(dict_by_dict.keys(), '\n')
print(dict_by_dict.values())

a = {'animal': 'elephant',
                'planet': 'dünya',
                'number': 40,
                'pi': 3.14,
                'is_good': True}

a.update({'is_bad': False})
a["hayvan"]= "kedi"
del a["planet"]
print(a)
print("is_bad" in a)
print("is_good" in a)

s = {"Harry": 29,
                "Clark": 32,
                "Peter": 22,
                "Bruce": 36
                }
print(s["Clark"])