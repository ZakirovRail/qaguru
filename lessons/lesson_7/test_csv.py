import csv

with open("username.csv") as csvfile:
    csvfile = csv.reader(csvfile)
    for r in csvfile:
        print(r)

with open("eggs.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Anna", "Pavel", "Peter"])
    csvwriter.writerow(["Alex", "Serj", "Sasha"])
