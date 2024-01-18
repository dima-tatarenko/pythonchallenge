# LIST COMPREHENSION

numbers = [1,2,3]

new_list = [n+1 for n in numbers]
print(new_list)

double_range = [n*2 for n in range(1,5)]

print(double_range)

names = ["Alex", "Beth", "Caroline", "James"]

new_names = [name.upper() for name in names if len(name) > 4]

print(new_names)