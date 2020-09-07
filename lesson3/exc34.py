list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
filteredList = range(0, 151, 5)
generalItems = set(filteredList) & set(list_of_six)
sortedList = sorted(list(generalItems))
print(sortedList)
