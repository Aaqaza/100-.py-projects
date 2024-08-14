# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

pass

# data = pandas.read_csv("weather_data.csv")

# print(type(data))
#
# print(type(data["temp"]))
#
# print(data.to_dict())

# temp_list = (data["temp"]).to_list()
# print(temp_list)

# avg = sum(data["temp"])/len(data["temp"])
# print(avg)

# OR

# print(data["temp"].mean())

# max_temp = data.temp.max()
# print(max_temp)

# print(data["condition"])
# print(data.condition)

# max_temp = max(data.temp)
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# temp = monday.temp
# temp_F = (temp * 9/5) + 32
#
# print(temp_F)


import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240813.csv")

data_frame = data["Primary Fur Color"].value_counts().to_frame()
csv = data_frame.to_csv("squirrel_count.csv")
print(type(data_frame))

# OR
# 
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# 
# print(gray_squirrel_count)
# print(red_squirrel_count)
# print(black_squirrel_count)
# 
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
# }
# 
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

