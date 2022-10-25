from  dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

f = pd.read_csv("GDP data.csv", encoding= "latin")
dp = pd.DataFrame(f)
dict2020 = {}
dict2021 = {}
dict2022 = {}
for i in dp.iterrows():
    dict2020[i[1]["Country"]] =  i[1]["2020"]
    dict2021[i[1]["Country"]] =  i[1]["2021"]
    dict2022[i[1]["Country"]] =  i[1]["2020.1"]

app = Dash(__name__)
dx = [ 'AVG(retail_and_recreation_percent_change_from_baseline)',
       'AVG(grocery_and_pharmacy_percent_change_from_baseline)',
       'AVG(parks_percent_change_from_baseline)',
       'AVG(transit_stations_percent_change_from_baseline)',
       'AVG(workplaces_percent_change_from_baseline)',
       'AVG(residential_percent_change_from_baseline)']
category_dropdown = dcc.Dropdown([
{"label": "Retail and Recreation", "value" : dx[0]},
{"label": "Grocery and Pharmacy" , "value" : dx[1]},
{"label": "Parks"                , "value" : dx[2]},
{"label": "Transit stations"     , "value" : dx[3]},
{"label": "Workplaces"           , "value" : dx[4]},
{"label": "Residential areas"    , "value" : dx[5]}]
, value = dx[0],id = "category-selector")


app.layout = html.Div(children= [
    html.H1(children = "Mobility data throughout a Pandemic"),
    html.Div(children= '''
    Time spent in Retail and recreational facilities compared to baseline'''),
    category_dropdown,
    html.Div(id="category-container"),
    dcc.Loading(dcc.Graph(id='Map-category', figure = {}), type="cube")
])

@app.callback(
    [Output('category-container', 'children'),
    Output('Map-category', component_property= 'figure')],
    Input('category-selector', 'value')
)

def update_output(value):
    container = f"Currently looking at {value} data"


    f = pd.read_parquet("Averages all categories", columns = ["Country", "date", str(value)])
    df = pd.DataFrame(f)
    df['date'] = pd.to_datetime(df['date'], )
    Final_df = df.groupby(["Country",pd.Grouper(freq="w",key = "date")]).mean()[value].reset_index()
    Final_df["GDP 2020"]= Final_df["Country"].map(dict2020)
    Final_df["GDP 2021"]= Final_df["Country"].map(dict2021)
    Final_df["GDP 2022"]= Final_df["Country"].map(dict2022)

    fig = px.scatter_geo(Final_df, locations= "Country", locationmode= "country names",
                        hover_name="Country", size= value,
                        animation_frame=Final_df.date.astype(str),
                        color = "GDP 2020",
                        projection="natural earth",
                        template = 'plotly_dark')

    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    fig.update_layout(height = 600)
    fig.update_layout(title = fig.layout.sliders[0].steps[0].label)
    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)


