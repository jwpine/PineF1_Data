import fastf1
import pandas as pd
import fastf1.core

fastf1.Cache.enable_cache('cache_spot')

year = 2022
grand_prix = 'Canadian Grand Prix'
grand_prix_day = 'Practice 1'

# Create the Session
session = fastf1.get_session(year, grand_prix, grand_prix_day)
session.load()

# Get the list of unique drivers in the session
drivers = pd.unique(session.laps['Driver'])

# Iterate through drivers to get all their lap data
df = []
for i in drivers:
    i_session = session.laps.pick_driver(i)
    df.append(i_session)
results = pd.concat(df)

# Print the results to an excel file
results.to_excel("C:/Users/johnp/Downloads/complete_session.xlsx")

