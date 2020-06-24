import csv
import json

source_file_path = 'data/state_population_data.csv'
target_file_path = 'data/state_population_data.json'
state_population_dict = {}

with open(source_file_path, 'r') as source_file:
    reader = csv.DictReader(source_file)
    
    for row in reader:
        state_population_dict[row['NAME']] = row['POPESTIMATE2019']

with open(target_file_path, 'w') as target_file:
    json.dump(state_population_dict, target_file)
