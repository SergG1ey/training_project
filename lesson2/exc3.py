if __name__ == '__main__':
    v = float(input("Вася speed: "))
    t = float(input("Вася time: "))
    l = v * t
    if 0 <= l <= 100:
        print("Вася rode:", l)
    elif l > 100:
        print(100, "Вася пролетел весь маршрут")
    else:
        print(0, "скорость не бывает минусовой) и время тоже")
