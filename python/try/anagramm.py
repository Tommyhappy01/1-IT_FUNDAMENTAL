liste=["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_list=[]
sonuc=[]

for i in liste:
  if sorted(i) not in sorted_list:
    sorted_list.append(sorted(i))
    
for a in range(len(sorted_list)):
  sonuc.append([i for i in liste if sorted(i)==sorted_list[a]])
print(sonuc)
