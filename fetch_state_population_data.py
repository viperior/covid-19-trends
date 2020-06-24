import requests

state_population_data_file_url = 'https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/national/totals/nst-est2019-alldata.csv'
target_data_file_path = 'data/state_population_data.csv'

r = requests.get(state_population_data_file_url)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
population_data = r.text
print('Saving data to ' + target_data_file_path + '...')

with open(target_data_file_path, 'w') as target_file:
    target_file.write(population_data)
