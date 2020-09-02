if __name__ == '__main__':
    x = float(input("Введите Х: "))
    if x > 0:
        print("sign(%s)=1" %(x))
    elif x < 0:
        print("sign(%s)=-1" %(x))
    else:
        print("sign(%s)=0" %(x))
