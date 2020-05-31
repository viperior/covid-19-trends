import pandas as pd
import plotly.express as px

def plot_bar_chart(chart_label, input_data_file_path, output_file_directory, x_axis_field_name, y_axis_field_name):
    output_file_name = chart_label.lower().replace(' ', '-')
    output_file_path = output_file_directory + '/' + output_file_name + '.html'
    df = pd.read_json(path_or_buf = input_data_file_path)
    fig = px.bar(df, x = x_axis_field_name, y = y_axis_field_name)
    fig.write_html(output_file_path)

# Plot new cases by time dimension attributes
input_data_file_path = 'data/daily_texas.json'
output_file_directory = 'sample'
y_axis_field_name = 'positiveIncrease'

plots = [
    ['date_label', 'Daily New Cases'],
    ['week_number_label', 'Weekly New Cases'],
    ['month_number_label', 'Monthly New Cases']
]

for plot in plots:
    plot_bar_chart(plot[1], input_data_file_path, output_file_directory, plot[0], y_axis_field_name)
