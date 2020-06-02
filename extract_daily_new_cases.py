import datetime
import operator
import pendulum
import json

# Load states to plot.
with open('data/states_to_plot.json', 'r') as states_to_plot_file:
    states_to_plot = json.load(states_to_plot_file)

# Load United States data set.
with open('data/daily.json', 'r') as input_file:
    json_data = json.load(input_file)

# Process each state's data.
for state in states_to_plot:
    filtered_json_data = [x for x in json_data if x['state'] == state['state_abbreviation']]
    
    for data_point in filtered_json_data:
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
        
        # Week Number
        week_number = date.isocalendar()[1]
        week_number_string = str(week_number).zfill(2)
        week_number_label = year_string + 'W' + week_number_string
        data_point['week_number_label'] = week_number_label
        
        # Week Start Date
        pendulum_date = pendulum.datetime(year_number, month_number, day_number, 0, 0, 0)
        week_start_date = pendulum_date.start_of('week')
        week_start_date_string = week_start_date.to_date_string()
        week_start_label = week_start_date_string
        data_point['week_start_label'] = week_start_label
        
    # Sort data chronologically (ascender order by date).
    filtered_json_data = sorted(filtered_json_data, key=operator.itemgetter('date'))
    
    # Save state-specific data file.
    with open('data/daily_' + state['state_name'].lower() + '.json', 'w') as output_file:
        json.dump(filtered_json_data, output_file)
