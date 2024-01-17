weather = "E:/Programming/Python/daily_python/25_pandas/weather_data.csv"


# with open(weather) as data_file:
#     report = data_file.readlines()
#     print(report)

# import csv

# temperatures = []

# with open(weather) as data_file:
#     report = csv.reader(data_file)
#     for row in report:
#         if row[1] != "temp":
#             print(row)
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

weather_data = pandas.read_csv(weather)

# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()

# print(data_dict)
# print(temp_list)

# print(data["temp"])

# total_temp = 0

# for temp in temp_list:
#     total_temp = total_temp + temp

# average = total_temp / (len(temp_list) -1)

# print(average)

highest_temp = weather_data.temp.max()
print(highest_temp)

print(weather_data[weather_data.day == "Monday"])
print(weather_data[weather_data.temp == weather_data.temp.max()])

Monday = weather_data[weather_data.day == "Monday"]

def fahrenheit(x):
    x = x * 1.8 + 32
    return float(x)

print(Monday.temp.apply(fahrenheit))