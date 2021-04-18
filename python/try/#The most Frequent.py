#The most Frequent
numbers = [-1,3,7,4,3,0,3,16,3,7,0,0,1]
e = max(1,2,3)
print(e)
empty = []
a = max(empty, default=True)
print(a)
b = max(empty, default="boş")
print(b)

sequence=[1,1,1,1,2,2,2,3,3,4]
c = max(sequence)
print(c)
d = sequence.count(1)
e = sequence.count(max(sequence))
print(d)
print(e)

numbers = [-1,11,7,4,11,0,11,16,11,7,0,0,11,11,11,3,11,1]
item = max(numbers,key = numbers.count)
h = numbers.count(item)
ı= numbers.count(max(numbers, key = numbers.count))

g = numbers.count(3)
print(item,h)
print(g)
print(ı)