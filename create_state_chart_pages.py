import dominate
from dominate.tags import *
import json

states_list_file_path = 'data/states_to_plot.json'

with open(states_list_file_path, 'r') as states_file:
    states_list = json.load(states_file)

for state in states_list:
    doc = dominate.document(title=state['state_name'] + ' - COVID-19 Trends')
    
    with doc.head:
        meta(charset='utf-8')
        meta(description='COVID-19 Trends')
        meta(author='Johnathon Stone')
        link(rel='stylesheet', href='./css/styles.css?v=1.0.1')
        link(rel='shortcut icon', type='image/x-icon', href='favicon.ico')
    
    h1(state['state_name'])
    
    with a(href='./index.html'):
        h2('Back to main page')
    
    for chart_type in ['daily', 'weekly', 'monthly']:
        chart_title = chart_type.capitalize() + ' New Cases ' + state['state_name']
        chart_file_path = './charts/' + chart_title.lower().replace(' ', '-') + '.html'
        
        with div(cls='chart'):
            iframe(src=chart_file_path, title=chart_title)

with open('docs/states/' + state['state_name'] + '.html', 'w') as f:
    f.write(doc.render())
