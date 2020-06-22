import json
import os
import requests

def extract_date(json):
    try:
        # Also convert to int since update_time will be string. When comparing
        # strings, "10" is smaller than "2".
        return int(json['date'])
    except KeyError:
        return 0

api_endpoint_url = 'https://covidtracking.com/api/v1/states/daily.json'
target_data_directory = 'data'
target_data_file_path = target_data_directory + '/daily.json'

print(api_endpoint_url)
r = requests.get(api_endpoint_url)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print('Saving data to ' + target_data_file_path + '...')

if not os.path.exists(target_data_directory):
    os.makedirs(target_data_directory)

with open(target_data_file_path, 'w') as target_data_file:
    json.dump(r.json(), target_data_file)
    
# Reload and sort the json file chronologically by date.
with open(target_data_file_path, 'r') as json_file:
    json_data = json.load(json_file)
    
json_data.sort(key=extract_date)

with open(target_data_file_path, 'w') as output_file:
    json.dump(json_data, output_file)
    
print('Data extraction complete.')
