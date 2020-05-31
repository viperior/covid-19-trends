import json
import requests

api_endpoint_url = 'https://covidtracking.com/api/v1/states/daily.json'
target_data_file_path = 'data/daily.json'

print(api_endpoint_url)
r = requests.get(api_endpoint_url)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print('Saving data to ' + target_data_file_path + '...')

with open(target_data_file_path, 'w') as target_data_file:
    json.dump(r.json(), target_data_file)
    
print('Data extraction complete.')
