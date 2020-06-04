import json
import pandas as pd
import plotly.express as px

def plot_bar_chart(chart_label, input_data_file_path, output_file_directory, x_axis_field_name, x_axis_label, y_axis_field_name, y_axis_label):
    output_file_name = chart_label.lower().replace(' - ', '-')
    output_file_name = output_file_name.replace(' ', '-')
    output_file_path = output_file_directory + '/' + output_file_name + '.html'
    df = pd.read_json(path_or_buf = input_data_file_path)
    fig = px.bar(df, x = x_axis_field_name, y = y_axis_field_name, text = y_axis_field_name)
    fig.layout.update(
        title = chart_label,
        xaxis_title = x_axis_label,
        yaxis_title = y_axis_label
    )
    fig.write_html(output_file_path)

# Load states to plot.
with open('data/states_to_plot.json', 'r') as states_to_plot_file:
    states_to_plot = json.load(states_to_plot_file)

for state in states_to_plot:
    print('Plotting data for ' + state['state_name'] + '...')
    
    # Plot new cases by time dimension attributes
    state_name_lower = state['state_name'].lower()
    input_data_file_path = 'data/daily_' + state_name_lower + '.json'
    output_file_directory = 'charts'
    y_axis_field_name = 'positiveIncrease'
    y_axis_label = 'New Cases'

    plots = [
        ['date_label', 'Daily New Cases - ' + state['state_name'], 'Date'],
        ['week_start_label', 'Weekly New Cases - ' + state['state_name'], 'Week'],
        ['month_number_label', 'Monthly New Cases - ' + state['state_name'], 'Month']
    ]
    
    for plot in plots:
        plot_bar_chart(
            chart_label = plot[1],
            input_data_file_path = input_data_file_path,
            output_file_directory = output_file_directory,
            x_axis_field_name = plot[0],
            x_axis_label = plot[2],
            y_axis_field_name = y_axis_field_name,
            y_axis_label = y_axis_label
        )
