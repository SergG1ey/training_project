import random
def play():
    i = 0
    result = 0
    while i < 3:
        x = int(input("Введите число от 1 до 10 : "))
        if 1 <= x <= 10:
            y = random.randint(1, 10)
            print("Рандомное число - ", y)
            if x == y: result += 1
            else: result -= 1
            if i == 2:
                if result >= 2 : print("you win")
                else: print("you lose")
        else:
            print("Вы ввели не правельные данные")
            play()
            break
        i += 1

play()

