import fastf1
import pandas as pd
import fastf1.core

fastf1.Cache.enable_cache('cache_spot')

# Create Session LIst
event_list_import = pd.read_csv("C:/Users/johnp/Downloads/Event_Rename.csv")
year = event_list_import["Year"].tolist()
grand_prix = event_list_import["EventName"].tolist()
grand_prix_day = event_list_import["Session Rename"].tolist()

# Create a starter index for interating through the data
index = 0
com_df = pd.DataFrame()

# Go through each session and get the data
for event in grand_prix:
    session = fastf1.get_session(year[index], grand_prix[index], grand_prix_day[index])
    session.load()
    laps = session.laps
    weather_data = session.laps.get_weather_data()
    laps = laps.reset_index(drop=True)
    weather_data = weather_data.reset_index(drop=True)
    event_list = {'Year': [year[index]], 'Grand_Prix': [grand_prix[index]], 'Event_List': [grand_prix_day[index]]}
    event_list_df = pd.DataFrame(event_list)
    event_list_df = event_list_df.loc[event_list_df.index.repeat(len(laps))].reset_index(drop=True)
    joined_df = pd.concat([laps, weather_data.loc[:, ~(weather_data.columns == 'Time')], event_list_df], axis=1)
    com_df = com_df.append(joined_df)
    index = index + 1

# Print the results to an excel file
com_df.to_csv("C:/Users/johnp/Downloads/season22.csv")