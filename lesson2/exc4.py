if __name__ == '__main__':
    x = int(input("Введите год: "))
    if x % 4 == 0 and x % 100 != 0 and x % 400:
        print("YES")
    else:
        print("NO")
