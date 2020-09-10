x = int(input("Введите х"))
y = int(input("Введите у"))
day = 0
while x < y:
    x = x / 100 * 110
    day = day + 1
print(day)
