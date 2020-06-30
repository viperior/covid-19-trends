import dominate
from dominate.tags import *
import json

doc = dominate.document(title='COVID-19 Trends')

with doc.head:
    meta(charset='utf-8')
    meta(description='COVID-19 Trends')
    meta(author='Johnathon Stone')
    link(rel='stylesheet', href='css/styles.css?v=1.0.1')
    link(rel='shortcut icon', type='image/x-icon', href='favicon.ico')
    link(rel='stylesheet', href='https://fonts.googleapis.com/css?family=Roboto+Condensed')
    link(rel='stylesheet', href='https://fonts.googleapis.com/css?family=Roboto')
    
states_list_file_path = 'data/states_to_plot.json'

with open(states_list_file_path, 'r') as states_file:
    states_list = json.load(states_file)

with doc:
    h1('COVID-19 Trends')
    a('Animated Choropleth for USA', href='animated_map.html')
    h2('State Charts')
    
    with div(cls='state-navigation'):
        with ul():
            for state in states_list:
                with li():
                    a(state['state_name'], href = 'states/' + state['state_name'] + '.html')
            
with open('docs/index.html', 'w') as f:
    f.write(doc.render())
