from datetime import date
def is_date(y, m, d):
    try:
        date(y, m, d)
        return True
    except ValueError:
        return False
d = int(input("введите день"))
m = int(input("введите месяц"))
y = int(input("введите год"))
print(is_date(y, m, d))


