import csv

csv_example = open("csv_example.csv")
csv_python = csv.reader(csv_example)


for row in csv_python:
    print("{} is in {} and has IP {}".format(row[0], row[2], row[1]))
