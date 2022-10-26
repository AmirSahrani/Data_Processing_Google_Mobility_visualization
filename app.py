from  dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

backgroundcolor = "#2d2c35"
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
{"label": "Residential areas"    , "value" : dx[5]}], value =dx[0] ,id = "category-selector", className = "dropdown_cat",clearable=False)
date_dropdown = dcc.Dropdown([2020,2021,2022], value = 2020,id = "date-selector", className = "dropdown_year", clearable=False)
value_to_label = {dx[0]:"Retail and Recreation",dx[1]:"Grocery and Pharmacy",dx[2]:"Parks",dx[3]: "Transit stations",dx[4]:"Workplaces",dx[5]:"Residential areas"}


app.layout = html.Div(children= [
    dbc.Row(dbc.Col(html.H1(children = "Mobility data throughout a Pandemic", style = {"color": "#78c2ad", "padding": 5}),
                width={"size":6, "offset": 3})),
    dbc.Row(dbc.Col(html.H5(children= '''
    Please select a category of location and the year to base the country GDP colors on''', style = {"color": "#f3969a", "padding": 5}),
                width={"size":5, "offset": 3})),
    dbc.Row([
        dbc.Col(html.Div(id = "graph-container", category_dropdown), 
            width = {"size" : 2, "offset" : 3}),
        dbc.Col(date_dropdown, 
            width = {"size" : 2, "offset" : 1})
        ]),
     dbc.Row(dbc.Col(html.H5(id="category-container", style = {"color": "#f3969a", "padding": 10}),
                width={"size":5, "offset": 3})),
    dbc.Row([dbc.Col(dcc.Loading(dcc.Graph(id='Map-category', figure = {}), type="cube", color = "#f3969a"),
                    width = {"size": 10,"offset":1}),
        ])
    
])

@app.callback(
    [Output('category-container', 'children'),
    Output('Map-category', component_property= 'figure')],
    [Input('category-selector', 'value'),
    Input('date-selector', 'value')])


def update_output(value,selected_date):
    container = f"Currently looking at the {value_to_label[value]} data, with the world wide GPD's showing for {selected_date}"


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
                        hover_data = {"Country": True, f"GDP {selected_date}": True, value: False},
                        color = f"GDP {selected_date}", color_continuous_scale = ["#78c2ad","#f3969a"])
    fig.update_layout(paper_bgcolor = backgroundcolor, plot_bgcolor = backgroundcolor,
                      margin=dict(l=0, r=0, t=0, b=0), height = 650,
                      font_color = "#ffffff")
    fig.update_geos(
    visible=False, resolution=50, showland = True, landcolor = "#d8d8d8",
    showocean = True, oceancolor = backgroundcolor)
    
    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)


