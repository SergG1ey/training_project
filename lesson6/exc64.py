import json
import datetime

with open("acdc.json") as file:
    my_file = json.load(file)

tracks = my_file['album']["tracks"]["track"]
sumDurations = 0

for i in tracks:
    sumDurations += int(i["duration"])

print(str(datetime.timedelta(seconds = sumDurations)))
