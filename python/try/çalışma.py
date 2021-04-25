mylist = ["eat", "tea", "tan", "ate", "nat", "bat"]

emptylist = []

for i in mylist:

    tempSet = set(i)

    templist = []

    
    for j in mylist:
   
        if  tempSet == tempSet.intersection(set(j)):
           templist.append(j)

    if templist not in emptylist:

            emptylist.append(templist)

    templist = []

print(emptylist)