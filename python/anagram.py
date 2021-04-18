anagram_list = []
word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
for word_1 in word_list:
    for word_2 in word_list:
        for word_3 in word_list:
            for word_4 in word_list:
                for word_5 in word_list:
                    for word_6 in word_list:
                        if word_1 != word_2 and (sorted(word_1) == sorted(word_2)):
                            elif word_2 != word_3 and (sorted(word_2) == sorted(word_3)):
                            anagram_list.append(word_1)
print(anagram_list)