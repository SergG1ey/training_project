list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
for i in range(0, 151):
    for k in list_of_six:
        if i == k and k % 5 == 0:
            print(k)
