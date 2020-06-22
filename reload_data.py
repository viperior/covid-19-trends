# Perform a full reload of COVID-19 new case data.

print('Beginning full reload of COVID-19 case data...')

# Retrieve the latest case data.
print('Retrieving data from COVID-19 tracking project...')
import fetch_historical_state_data
print('Latest case data retrieved!')

# Refresh the list of states to plot data for.
print('Updating the list of dates to plot...')
import create_states_to_plot_json
print('State list updated!')

# Extract and transform data.
print('Transforming data and adding features (go pandas, go!)...')
import extract_daily_new_cases
print('Data is ready!')

# Refresh charts.
print('Plotting data charts using plotly...')
import plot_new_cases
import create_animated_map
import create_chart_web_page
import build_web_pages
print('Charts updated!')

print('Data reload complete!')
