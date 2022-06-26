import fastf1
import pandas as pd
import fastf1.core

fastf1.Cache.enable_cache('cache_spot')
year = 2022

# Get the Complete Event List
event_list = fastf1.get_event_schedule(year)


# send event list to csv
event_list.to_csv("C:/Users/johnp/Downloads/events.csv")

# Read csv to new dataframe because Fastf1 is a bit dumb
event_list_df = pd.read_csv("C:/Users/johnp/Downloads/events.csv")

# Repeat lines 5 times to get each session as a new line
mid_df = event_list_df.loc[event_list_df.index.repeat(5)].reset_index(drop=True)
mid_df.to_excel("C:/Users/johnp/Downloads/events_DF.xlsx")

# Create a loop that drops columns