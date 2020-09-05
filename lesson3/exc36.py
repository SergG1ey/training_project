x = int(input("Введите начальное положение x: "))
y = int(input("Введите начальное положение y: "))

x1 = int(input("Введите координаты следующей клетки x: "))
y1 = int(input("Введите координаты следующей клетки y: "))

while 0 < (x or x1 or y or y1) > 9:
    print("вы ввели не верные координаты(1-8)\n")
    x = int(input("Введите начальное положение x: "))
    y = int(input("Введите начальное положение y: "))

    x1 = int(input("Введите координаты следующей клетки x: "))
    y1 = int(input("Введите координаты следующей клетки y: "))

modulX = abs(x - x1)
modulY = abs(y - y1)

if modulX == 1 and modulY ==2 or modulX == 2 and modulY == 1:
    print("конь попал")
else:
    print("конь не попал")




