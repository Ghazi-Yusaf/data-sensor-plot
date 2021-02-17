import json, sys, fileinput

print('Enter the path of the data file to read:')

with open(input()) as dataText:
    data = json.load(dataText)

startDate = data['data_range']['minimum_date'].replace('T', ' ').split('.')[0]
endDate = data['data_range']['maximum_date'].replace('T', ' ').split('.')[0]

totalTemperature = 0
totalHumidity = 0
totalCO2 = 0
count = 0

for (k, v) in data['data'].items():
    count += 1
    totalTemperature += data['data'][f'{k}']['944']['temperature']
    totalHumidity += data['data'][f'{k}']['944']['humidity']
    totalCO2 += data['data'][f'{k}']['944']['co2']

averageTemperature = totalTemperature / count
averageHumidity = totalHumidity / count
averageCO2 = totalCO2 / count

print(f'\nAverage Temperature: {averageTemperature}\nAverage Humidity: {averageHumidity}\nAverage CO2: {averageCO2}')

# print(f'enter a time frame between {startDate} and {endDate} to produce output:')

# print('Start:')
# userStart = input()

# print('End:')
# userEnd = input()

# temperature, humidity, co2.