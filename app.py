from  dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
dx = pd.DataFrame(columns =
      ['AVG(retail_and_recreation_percent_change_from_baseline)',
       'AVG(grocery_and_pharmacy_percent_change_from_baseline)',
       'AVG(parks_percent_change_from_baseline)',
       'AVG(transit_stations_percent_change_from_baseline)',
       'AVG(workplaces_percent_change_from_baseline)',
       'AVG(residential_percent_change_from_baseline)'])
category_dropdown = dcc.Dropdown([
{"label": "Retail and Recreation", "value" : dx.columns[0]},
{"label": "Grocery and Pharmacy" , "value" : dx.columns[1]},
{"label": "Parks"                , "value" : dx.columns[2]},
{"label": "Transit stations"     , "value" : dx.columns[3]},
{"label": "Workplaces"           , "value" : dx.columns[4]},
{"label": "Residential areas"    , "value" : dx.columns[5]}]
, value = dx.columns[0],id = "category-selector")

app.layout = html.Div(children= [
    html.H1(children = "Mobility data throughout a Pandemic"),
    html.Div(children= '''
    Time spent in Retail and recreational facilities compared to baseline'''),
    category_dropdown,
    html.Div(id="category-container"),
    dcc.Graph(id='Map-category', figure = {}),
    # dcc.Loading(dcc.Graph(id="graph"), type="cube")
    
])

@app.callback(
    [Output('category-container', 'children'),
    Output('Map-category', component_property= 'figure')],
    Input('category-selector', 'value')
)

def update_output(value):
    f = pd.read_parquet("Averages all categories", columns = ["country_region_code", "date", str(value)])
    df = pd.DataFrame(f)
    container = f"Currently looking at {value} data"
    fig = px.scatter_geo(df, locations="country_region_code",
                        hover_name="country_region_code", size= value,
                        animation_frame="date",
                        animation_group="country_region_code",
                        projection="natural earth",
                        template = 'plotly_dark',
                        redraw = False)
    fig.update_layout(transition = {'duration': 1})
    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)


