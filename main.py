import json

with open('data/2021-01-17 22 05.txt') as dataText:
    data = json.load(dataText)

print(data['data']['2021-01-10 07:20:00 UTC']['944']['co2'])