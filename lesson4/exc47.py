oneList = [9, 4, 6, 2, 5, 7, 1]
twoList = [5, 7, 3, 8, 4, 1]
indList = set(oneList) | set(twoList)
uni_oneList = set(oneList) - set(twoList)
iList = set(oneList) & set(twoList)
uniList = indList - iList
print(indList,"\n", uni_oneList, "\n", uniList)

