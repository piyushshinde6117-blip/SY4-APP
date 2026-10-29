import csv
import json

# Open the CSV file
with open("data.csv", "r") as csv_file:

    # Read CSV data
    csv_reader = csv.DictReader(csv_file)

    # Convert CSV data into a list
    data = list(csv_reader)

# Open JSON file for writing
with open("output.json", "w") as json_file:

    # Convert data into JSON format
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON!")