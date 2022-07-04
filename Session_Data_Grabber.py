import fastf1
import pandas as pd
import fastf1.core

fastf1.Cache.enable_cache('cache_spot')

year = 2022
grand_prix = 'British Grand Prix'
grand_prix_day = 'Practice 2'

# Create the Session
session = fastf1.get_session(year, grand_prix, grand_prix_day)
session.load()

# Get the laps and weather
laps = session.laps
weather_data = session.laps.get_weather_data()
laps = laps.reset_index(drop=True)
weather_data = weather_data.reset_index(drop=True)
event_list = {'Year': [year], 'Grand_Prix': [grand_prix], 'Event_List': [grand_prix_day]}
event_list_df = pd.DataFrame(event_list)
event_list_df = event_list_df.loc[event_list_df.index.repeat(len(laps))].reset_index(drop=True)

# exclude the 'time' column from weather and join the weather, laps, and event name together
joined_data = pd.concat([laps, weather_data.loc[:, ~(weather_data.columns == 'Time')], event_list_df], axis=1)

# Print the results to an excel file
joined_data.to_excel("C:/Users/johnp/Downloads/playground2.xlsx")


