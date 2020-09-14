def is_prime(a, b):
    if figure == 1:
        return (a * b) / 2
    else:
        return a * b

a = int(input("введите число1: "))
b = int(input("введите число2: "))
figure = int(input("1- треугольник \n2- квадрат \n"))

print(is_prime(a, b))

