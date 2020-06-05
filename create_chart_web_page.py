import dominate
from dominate.tags import *
import json

doc = dominate.document(title='COVID-19 Trends')

with doc.head:
    meta(charset='utf-8')
    meta(description='COVID-19 Trends')
    meta(author='Johnathon Stone')
    link(rel='stylesheet', href='css/styles.css?v=1.0.1')

states_list_file_path = 'data/states_to_plot.json'

with open(states_list_file_path, 'r') as states_file:
    states_list = json.load(states_file)

with doc:
    h1('COVID-19 Trends')
    
    for state in states_list:
        h2(state['state_name'])
        
        for chart_type in ['daily', 'weekly', 'monthly']:
            chart_title = chart_type.capitalize() + ' New Cases ' + state['state_name']
            chart_file_path = 'charts/' + chart_title.lower().replace(' ', '-') + '.html'
            
            with div(cls='chart'):
                iframe(src=chart_file_path, title=chart_title)

with open('index.html', 'w') as f:
    f.write(doc.render())
