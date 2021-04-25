#C8381-Tommy

# The largest number program: example:
#n = 3, 67 85 19      The largest number is:  85"""

print("""
#####################################
#       Find The Largest Number     #
#             Program               #
#####################################
""")

n = int(input("kaç numara gireceksin? : "))
numbers = list()
for i in range(0,n):
    numbers.append(int(input("numara giriniz: ")))
    numbers.sort()
print("the largest number is: ", numbers[-1])

# Second exp. The largest number program:
#n = 5, 1 2 3 4 5     The largest number is:  5
num_first  = int(input("Please enter number: "))    #kullanıcıdan alınan sayıları  
num_second = int(input("Please enter number: "))    #karşılaştırıp atama yapacağız.
num_third  = int(input("Please enter number: "))
num_fourth = int(input("Please enter number: "))
num_fifth  = int(input("Please enter number: "))

if (num_first > num_second) and (num_first > num_third) and (num_first > num_fourth) and (num_first > num_fifth):
    largest_number = num_first
elif (num_second > num_first) and (num_second > num_third) and (num_second > num_fourth) and (num_second > num_fifth):
    largest_number = num_second
elif (num_third > num_first) and (num_third > num_second) and (num_third > num_fourth) and (num_third > num_fifth):
    largest_number = num_third
elif (num_fourth > num_first) and (num_fourth > num_second) and (num_fourth > num_third) and (num_fourth > num_fifth):
    largest_number = num_fourth
else:
    largest_number = num_fifth
print("Largest number is :", largest_number )


number = int(input("How many numbers will you enter? "))
sayılar = []
for i in range(number):
    x = int(input("Please enter the number: "))
    sayılar.append(x)
sayılar.sort(reverse = True)
print("The largest number is:", sayılar[0])

number = int(input("How many numbers will you enter? "))
sayılar = []
for i in range(number):
    x = int(input("Please enter the number: "))
    sayılar.append(x)
sayılar.sort()
print("The largest number is:", sayılar[-1])
