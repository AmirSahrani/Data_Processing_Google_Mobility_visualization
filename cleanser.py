import pandas as pd
f = pd.read_csv("C:\\Users\\amisa\\Documents\\Python\\Final Project\\2022_All_Countries_Region_Mobility_Report.csv")
df = pd.DataFrame(f)

df.head(50).to_clipboard()