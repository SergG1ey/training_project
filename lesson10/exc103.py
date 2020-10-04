my_list = list(input("ведите лист"))
n_element = int(input())

def shift(my_list, step):
    if step < 0:
        step = abs(step)
        for i in range(step):
            my_list.append(my_list.pop(0))
    else:
        for i in range(step):
            my_list.insert(0, my_list.pop())


shift(my_list, n_element)
print(my_list)
