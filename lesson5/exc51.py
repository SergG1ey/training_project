
def is_prime(x):
    d = 2
    while x % d != 0:
        d+=1
    return x == d

x = int(input("введите число от 1 до 1000:"))
if 1 <= x <= 1000:
  print(is_prime(x))

else:
    print("вы ввели неверное число")
