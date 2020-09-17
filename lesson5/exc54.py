my_list = [4, 6, 7, 9, 2, 1, 4, 3, 2, 6, 5, 9, 14, 15, 7, 7]
count = 0
for i in my_list:
    if i % 2 != 0:
        index = my_list.index(i)
        my_list[index]=0
        count += 1

print(my_list,"\n", count)