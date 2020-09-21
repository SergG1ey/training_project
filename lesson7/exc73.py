import requests
import datetime

API_KEY = "f9ada9efec6a3934dad5f30068fdcbb8"
s_city = input("Введите город:")
cnt = int(input("Количество дней"))

url = "http://api.openweathermap.org/data/2.5/forecast/daily"
params = {"q": s_city, "cnt": cnt, "appid": API_KEY, "units": "metric"}

res = requests.get(url, params)
data = res.json()

f = open("21-09-2020-Odessa-5-days-weather-forecast.txt", "w")
weathers = data["list"]
f.write("Date        Temp day    Temp feels like     Temp night\n")

for i in weathers:
    date = datetime.datetime.fromtimestamp(i["dt"]).strftime("%d-%m-%Y")
    tempDay = str(i["temp"]["day"])
    tempFeels = str(i["feels_like"]["day"])
    tempNight = str(i["temp"]["night"])
    row = date + '\t' + tempDay + '\t\t' + tempFeels + '\t\t\t\t' + tempNight + '\n'
    f.write(row)

f.close()
