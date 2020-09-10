import math
x = int(input("Введите число: "))
print(math.factorial(x))

i = 1
fuck = 1
while i <= x:
    fuck = i * fuck
    i = i + 1
print(fuck)