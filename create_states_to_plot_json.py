import json

output_file_path = 'data/states_to_plot.json'

states_to_plot = [
    {
        'state_abbreviation': 'TX',
        'state_name': 'Texas'
    },
    {
        'state_abbreviation': 'MI',
        'state_name': 'Michigan'
    }
]

with open(output_file_path, 'w') as output_file:
    json.dump(states_to_plot, output_file)
