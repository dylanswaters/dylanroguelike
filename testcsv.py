import csv

input = csv.DictReader(open("text/meleeWeapons.csv"))

for item in input:
    print(item)
    print(type(item))

print(input[0])
