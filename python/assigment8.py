#C8381-Tommy

# The largest number program: example:
#n = 5, 1 2 3 4 5     The largest number is:  5
#n = 3, 67 85 19      The largest number is:  85"""

print("""
#####################################
#       Find The Largest Number     #
#             Program               #
#####################################
""")
num_first  = int(input("Please enter number: "))    #kullanıcıdan alınan sayıları  
num_second = int(input("Please enter number: "))    #karşılaştırıp atama yapacağız.
num_third  = int(input("Please enter number: "))
num_fourth = int(input("Please enter number: "))
num_fifth  = int(input("Please enter number: "))

if (num_first > num_second) and (num_first > num_third) and (num_first > num_fourth) and (num_first > num_fifth):
    largest_number = num_first
if (num_second > num_first) and (num_second > num_third) and (num_second > num_fourth) and (num_second > num_fifth):
    largest_number = num_second
elif (num_third > num_first) and (num_third > num_second) and (num_third > num_fourth) and (num_third > num_fifth):
    largest_number = num_third
elif (num_fourth > num_first) and (num_fourth > num_second) and (num_fourth > num_third) and (num_fourth > num_fifth):
    largest_number = num_fourth
else:
    largest_number = num_fifth
print("Largest number is :", largest_number )


# Group Anagrams: example:
# ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:[["ate","eat","tea"], ["nat","tan"], ["bat"]]  

anagram_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Python3 program for the above approach
from collections import Counter
 
# function to check if two strings are
# anagram or not
def check(anagram_list["ate","eta","tae"]):
   
    # implementing counter function
    if(Counter(anagram_list) == Counter(anagram_list)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
 
 
