n = int(input("how many times will you enter"))
numbers = list()
for i in range(0,n):
    numbers.append(int(input("enter your number: ")))
numbers.sort()
print("the largest number is: ", numbers[-1])

