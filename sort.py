import csv
dataset = []
with open("dataset2.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset.append(row)

headers = dataset[0]
planet_data = dataset[1:]

for data in planet_data:
    data[2] = data[2].lower()

planet_data.sort(key=lambda planet_data: planet_data[2])

with open("dataset2sorted.csv", "a+") as f:
    CSVwriter = csv.writer(f)
    CSVwriter.writerow(headers)
    CSVwriter.writerows(planet_data)