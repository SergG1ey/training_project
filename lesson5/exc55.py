from math import sqrt
def square(number):
    perimeter = number * 4
    area = number * number
    diagonal = number * sqrt(2)
    return perimeter, area, diagonal
x = int(input("Введите строрну квадрата: "))
print(square(x))
