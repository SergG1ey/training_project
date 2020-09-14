from math import sqrt
def square():
    perimeter = x * 4
    area = x * x
    diagonal = x * sqrt(2)
    return perimeter, area, diagonal
x = int(input("Введите строрну квадрата: "))
print(square())
