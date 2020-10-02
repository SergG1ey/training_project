import requests
import json
import datetime
import argparse

def convertor(_from, _to, date_string, amount):
    format_date = "%Y-%m-d"
    today = datetime.date.today().strftime(format_date)

    try:
        d = datetime.datetime.strptime(date_string, format_date)
        if d > datetime.datetime.strptime(today, format_date):
            date_string = today
    except ValueError:
        date_string = today

    with open("symbols.json") as file:
        symbols = json.load(file)

    try:
        condition = symbols["symbols"][_from] or symbols["symbols"][_to]
        url = "https://api.exchangerate.host/convert"
        params = {"from": _from, "to": _to, "amount": amount, "date": date_string}

        res = requests.get(url, params)
        data = res.json()

        f = open("start_date == 2020-09-18.txt", "w")
        f.write('[["date", "from", "to", "amount", "rate", "result"],\n')

        date = data["date"]
        res_from = data["query"]["from"]
        to = data["query"]["to"]
        res_amount = str(data["query"]["amount"])
        rate = str(data["info"]["rate"])
        result = str(data["result"])

        row = ' ["' + date + '", "' + res_from + '", "' + to + '", "' + res_amount + '", "' + rate + '", "' + result + '"]]'
        f.write(row)
    except KeyError:
        print('wrong data')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--custom_from", default="USD")
    parser.add_argument("--to", default="UAH")
    parser.add_argument("date")
    parser.add_argument("amount")
    args = parser.parse_args()
    convertor(args.custom_from, args.to, args.date, args.amount)
