temp = int(input("введите температуру:"))
temp_type = input("Введите шкалу измерения C, F, K:")
if temp_type == "C":
    print("C: ", temp, "\nF: ", temp * 1.8 + 32, "\nK: ", temp + 273.15)
elif temp_type == "F":
    print("C: ", (temp - 32)/1.8, "\nF: ", temp, "\nK: ", (temp + 459.67)/1.8)
elif temp_type == "K":
    print("C ", temp - 273.15, "\nF: ", temp * 1.8 - 459.67, "\nK: ", temp)
else:
    print("неверные данные")
