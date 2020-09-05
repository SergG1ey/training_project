import random
x = int(input("Введите число от 1 до 10 : "))
if 1 <= x <= 10:
    y = random.randint(1, 10)
    if x == y:
        print("you win", x, "=", y)
    else:
        print("you lose!", x, "!=", y)
else:
    print("Вы ввели не правельные данные")
