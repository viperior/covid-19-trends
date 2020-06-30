import datetime
import json
import os
import pandas as pd
import plotly.express as px  # Be sure to import express

print('Creating animated choropleth map of USA data...')
df = pd.read_json(path_or_buf = 'data/daily.json')

# Transform the integer date column into a timestamp.
df['date'] = df.apply(lambda row: datetime.datetime.strptime(str(row.date), '%Y%m%d'), axis = 1)

# Define the date boundaries.
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(60)

# Filter the time range of the data.
mask = (df['date'] > start_date) & (df['date'] <= end_date)
df = df.loc[mask]

# Create a column representing the frame number in the animation using the date.
df['frame'] = df.apply(lambda row: (row.date - start_date).days, axis = 1)

# Determine the maximum new daily positive test result within the restricted time frame.
positive_increase_column = df['positiveIncrease']
max_positive_increase = positive_increase_column.max()
print('Max positive increase = ' + str(max_positive_increase))

fig = px.choropleth(
    df,  # Input Pandas DataFrame
    locations = 'state',  # DataFrame column with locations
    color_continuous_scale = 'redor',
    range_color = (0, max_positive_increase),
    color = 'positiveIncrease',  # DataFrame column with color values
    hover_name = 'date', # DataFrame column hover info
    animation_frame = 'frame',
    locationmode = 'USA-states' # Set to plot as US States
)
fig.update_layout(
    title_text = 'Positive Cases By State', # Create a Title
    geo_scope = 'usa',  # Plot only the USA instead of globe
)
fig.write_html('docs/charts/animated-map-usa.html')
