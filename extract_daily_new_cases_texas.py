import datetime
import operator
import json

with open('data/daily.json', 'r') as input_file:
    json_data = json.load(input_file)

json_data = [x for x in json_data if x['state'] == 'TX']

for data_point in json_data:
    # Year
    year_string = str(data_point['date'])[:4]
    year_number = int(year_string)
    
    # Month
    month_number_string = str(data_point['date'])[4:6]
    month_number = int(month_number_string)
    month_number_label = year_string + '-' + month_number_string
    data_point['month_number_label'] = month_number_label
    
    # Date / Day
    day_number_string = str(data_point['date'])[6:]
    day_number = int(day_number_string)
    date_label = month_number_label + '-' + day_number_string
    data_point['date_label'] = date_label
    date = datetime.date(year_number, month_number, day_number)
    
    # Week
    week_number = date.isocalendar()[1]
    week_number_string = str(week_number).zfill(2)
    week_number_label = year_string + 'W' + week_number_string
    data_point['week_number_label'] = week_number_label
    
json_data = sorted(json_data, key=operator.itemgetter('date'))

with open('data/daily_texas.json', 'w') as output_file:
    json.dump(json_data, output_file)
