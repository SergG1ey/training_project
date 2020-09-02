if __name__ == '__main__':
    y = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    x = float(input("Введите х: "))
    value = str(x)
    isPresent = ""
    for i in y:
        if value.find("%s." %(i) ) != -1:
            isPresent = "HAVE"
            break
        else:
            isPresent = "HAVE NOT"

    print(isPresent)
