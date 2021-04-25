mylist = ["eat", "tea", "tan", "ate", "nat", "bat"]

emptylist = []

for i in mylist:

    tempSet = set(i)

    templist = []

    for j in range(len(mylist)):

        if tempSet == tempSet.intersection(set(mylist[j])):

            templist.append(mylist[j])

    if templist not in emptylist:

            emptylist.append(templist)

    templist = []

print(emptylist)





