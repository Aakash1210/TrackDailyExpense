import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file and convert it to a list of dictionaries
    data = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Write the data to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

# Paths to the CSV and JSON files
csv_file_path = '/Users/rajendrachauhan/Downloads/transport.csv'
json_file_path = '/Users/rajendrachauhan/Downloads/transport.json'

# Convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)

# import json

# import json

# def add_ids_to_json(json_file_path):
#     # Read the JSON file
#     with open(json_file_path, mode='r', encoding='utf-8') as file:
#         data = json.load(file)

#     # Add incrementing ids to each dictionary in the JSON data
#     for idx, item in enumerate(data, start=4):
#         item['id'] = idx

#     # Write the updated data back to the JSON file
#     with open(json_file_path, mode='w', encoding='utf-8') as file:
#         json.dump(data, file, indent=4)

#     # Print the updated data (optional)
#     print(json.dumps(data, indent=4))

# json_file_path = '/Users/rajendrachauhan/Downloads/expense.json'
# add_ids_to_json(json_file_path)