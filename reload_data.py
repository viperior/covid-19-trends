# Perform a full reload of COVID-19 new case data.

print('Beginning full reload of COVID-19 case data...')

# Retrieve the latest case data.
import fetch_historical_state_data

# Refresh the list of states to plot data for.
import create_states_to_plot_json

# Extract and transform data.
import extract_daily_new_cases

# Refresh charts.
import plot_new_cases

print('Data reload complete! 🌟')
