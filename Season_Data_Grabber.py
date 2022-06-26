import fastf1
import pandas as pd
import fastf1.core

fastf1.Cache.enable_cache('cache_spot')
# DataFrame to put all results
laps_df = []

# Read the list of events and grab the right columns to get every session
event_list_df = pd.read_csv("C:/Users/johnp/Downloads/Event_Rename.csv")
year = event_list_df["Year"].tolist()
grand_prix = event_list_df["EventName"].tolist()
day = event_list_df["Session Rename"].tolist()

# Create a starter to iterate through each event
index = 0

# Go through each session and create the session characteristics
for event in grand_prix:
    session = fastf1.get_session(year[index], grand_prix[index], day[index])
    session.load()
    drivers = pd.unique(session.laps['Driver'])
    for i in drivers:
        i_session = session.laps.pick_driver(i)
        laps_df.append(i_session)
    results = pd.concat(laps_df)
    index = index + 1

# Print the results to an xlsx
results.to_excel("C:/Users/johnp/Downloads/combined_laps.xlsx")





