import datetime
import operator
import json

with open('data/daily.json', 'r') as input_file:
    json_data = json.load(input_file)

json_data = [x for x in json_data if x['state'] == 'TX']

for data_point in json_data:
    year_string = str(data_point['date'])[:4]
    year = int(year_string)
    month_number_string = str(data_point['date'])[4:6]
    month_number = int(month_number_string)
    day_number_string = str(data_point['date'])[6:]
    day_number = int(day_number_string)
    date_string = year_string + '-' + month_number_string + '-' + day_number_string
    data_point['date_string'] = date_string
    date = datetime.date(year, month_number, day_number)
    week_number = date.isocalendar()[1]
    week_number_string = year_string + 'W' + str(week_number)
    data_point['week_number_string'] = week_number_string
    
json_data = sorted(json_data, key=operator.itemgetter('date'))

with open('data/daily_texas.json', 'w') as output_file:
    json.dump(json_data, output_file)
