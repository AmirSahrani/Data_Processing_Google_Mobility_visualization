from  dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

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


    f = pd.read_parquet("Averages all categories", columns = ["country_region_code", "date", str(value)])
    df = pd.DataFrame(f)
    df['date'] = pd.to_datetime(df['date'])
    df1 = df.groupby(["country_region_code",pd.Grouper(freq="w",key = "date")]).mean()[value].reset_index()
    fig = px.scatter_geo(df1, locations= "country_region_code",
                        hover_name="country_region_code", size= value,
                        animation_frame=df1.date.astype(str),
                        projection="natural earth",
                        template = 'plotly_dark')
    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)


