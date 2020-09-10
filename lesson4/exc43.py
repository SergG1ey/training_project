a = int(input("Введите первое числo: "))
b = int(input("Введите второе числo: "))

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
