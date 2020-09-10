import random
i = 0
result = 0
while i < 3:
    x = int(input("Введите число от 1 до 10 : "))
    if 1 <= x <= 10:
        y = random.randint(1, 10)
        print("Рандомное число - ", y)
        if result == y : print("you win")
        else: print("you lose")
    else:
        print("Вы ввели не правельные данные")
    i += 1


