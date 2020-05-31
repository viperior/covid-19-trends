import pandas as pd
import plotly.express as px

df = pd.read_json(path_or_buf = 'data/daily_texas.json')
fig = px.bar(df, x = 'week_number_label', y = 'positiveIncrease')
fig.write_html('sample/daily-new-cases-texas.html')
