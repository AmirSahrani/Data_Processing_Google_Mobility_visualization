import pandas as pd
import os
cwd = os.getcwd()

directory= 'C:\\Users\\amisa\\Documents\\Python\\Final Project'
os.chdir(directory)
directory_list = os.listdir(directory)
csv_list = [x for x in directory_list if x[-4:] == ".csv"]

df = pd.DataFrame(columns=["country_region_code","date","retail_and_recreation_percent_change_from_baseline","grocery_and_pharmacy_percent_change_from_baseline","parks_percent_change_from_baseline","transit_stations_percent_change_from_baseline","workplaces_percent_change_from_baseline","residential_percent_change_from_baseline"])

for i in csv_list:
    f = pd.read_csv(i, low_memory = False)
    df_new = pd.DataFrame(f,columns=["country_region_code","date","retail_and_recreation_percent_change_from_baseline","grocery_and_pharmacy_percent_change_from_baseline","parks_percent_change_from_baseline","transit_stations_percent_change_from_baseline","workplaces_percent_change_from_baseline","residential_percent_change_from_baseline"])
    df = pd.concat([df,df_new])

df.to_csv("C:\\Users\\amisa\\Documents\\Python\\Final Project\\2022_All_Countries_Region_Mobility_Report.csv",index = False)