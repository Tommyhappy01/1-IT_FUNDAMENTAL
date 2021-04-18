# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 12:43:48 2021

@author: ÖKTEN
"""

school_records={
    "personal_info":
        {"kid":{"tom": {"class": "intermediate", "age": 10},
                "sue": {"class": "elementary", "age": 8}
               },
         "teen":{"joseph":{"class": "college", "age": 19},
                 "marry":{"class": "high school", "age": 16}
               },
        },
    "grades_info":
        {"kid":{"tom": {"math": 88, "speech": 69},
                "sue": {"math": 90, "speech": 81}
               },
         "teen":{"joseph":{"coding": 80, "math": 89},
                 "marry":{"coding": 70, "math": 96}
               },
        },
}

print(school_records["personal_info"])
print(school_records["personal_info"]["teen"])
print(school_records["personal_info"]["teen"]["marry"])
print(school_records["personal_info"]["teen"]["marry"]["age"])
print(school_records["grades_info"]["teen"]["joseph"])       # sözlük olarak
print(list(school_records["grades_info"]["teen"]["joseph"].items())) #liste içinde tuple yaptık
