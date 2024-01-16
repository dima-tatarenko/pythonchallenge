textpath = "e:/Programming/Python/daily_python/24_edit_file/test.txt"

# mode w = write
# mode a = append

with open(textpath, mode="w") as file:
    contents = file.write("Meow")
    print(contents)


