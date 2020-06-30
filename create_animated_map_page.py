import dominate
from dominate.tags import *
import json

doc = dominate.document(title='Animated Map of USA Outbreak - COVID-19 Trends')

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
    with a(href='index.html'):
        h1('COVID-19 Trends')

    h2('Animated Choropleth for USA')
    
    with div(cls='chart'):
        iframe(src='charts/animated-map-usa.html', title='USA Animated Choropleth Map')
    
with open('docs/animated_map.html', 'w') as f:
    f.write(doc.render())
