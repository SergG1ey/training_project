my_list = [4, 6, 7, 9, 2, 1, 4, 3, 2, 6, 5, 9, 14, 15, 7, 7]
zero_list = []
count = 0
for i in my_list:
    if i % 2 != 0:
        zero_list.append(0)
        count += 1
    else:
        zero_list.append(i)
print(zero_list, count)