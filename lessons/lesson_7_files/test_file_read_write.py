with open("resources/text", "w") as file:
    file.write("abbc\n")

with open("resources/text") as file:
    for row in file:
        print(row)
