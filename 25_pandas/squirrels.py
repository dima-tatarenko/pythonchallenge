import pandas

squirrel_csv = "E:/Programming/Python/daily_python/25_pandas/squirrel_data.csv"

squirrel_data = pandas.read_csv(squirrel_csv)

# print(weather_data[weather_data.day == "Monday"])

gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]) -1
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]) -1
cinnamon_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]) -1

print(gray_squirrel_count)
print(black_squirrel_count)
print(cinnamon_squirrel_count)


squirrel_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(squirrel_data_dict)
df.to_csv("squirrel_count.csv")
