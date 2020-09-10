my_list = [4, 7, 6, 8, 7, 9, 3, 4, 7, 9, 1, 3, 7, 8]
n = len(my_list)
count = 0
for i in my_list:
    if 0 < i < n - 1 and my_list[i - 1] > my_list[i] < my_list[i + 1]:
        count += 1
print("количество элементов которые меньше двух своих соседей: ", count)

