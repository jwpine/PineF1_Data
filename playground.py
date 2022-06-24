import fastf1
import pandas as pd
import fastf1.core

fastf1.Cache.enable_cache('cache_spot')
year = 2022

# Get the Complete Event List
event_list = fastf1.get_event_schedule(year)

#print(event_list)
#event_list.to_excel("C:/Users/johnp/Downloads/events.xlsx")