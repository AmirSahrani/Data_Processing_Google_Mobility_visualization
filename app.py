from  dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
# Setting up some objects I will need later 
dx = [ 'AVG(retail_and_recreation_percent_change_from_baseline)',
       'AVG(grocery_and_pharmacy_percent_change_from_baseline)',
       'AVG(parks_percent_change_from_baseline)',
       'AVG(transit_stations_percent_change_from_baseline)',
       'AVG(workplaces_percent_change_from_baseline)',
       'AVG(residential_percent_change_from_baseline)']
#Names in my data frame are different to the labels, this is a round about way of making sure everything is consistent on the front end
value_to_label = {dx[0]:"Retail and Recreation",dx[1]:"Grocery and Pharmacy",dx[2]:"Parks",dx[3]: "Transit stations",dx[4]:"Workplaces",dx[5]:"Residential areas"}
backgroundcolor = "#2d2c35"

# Loading the data I will be needing later for GDP's
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

#Creating the dropdowns
category_dropdown = dcc.Dropdown([
{"label": "Retail and Recreation", "value" : dx[0]},
{"label": "Grocery and Pharmacy" , "value" : dx[1]},
{"label": "Parks"                , "value" : dx[2]},
{"label": "Transit stations"     , "value" : dx[3]},
{"label": "Workplaces"           , "value" : dx[4]},
{"label": "Residential areas"    , "value" : dx[5]}], value =dx[0] ,id = "category-selector", className = "dropdown_cat",clearable=False)
date_dropdown = dcc.Dropdown([2020,2021,2022], value = 2020,id = "date-selector", className = "dropdown_year", clearable=False)
graph_dropdown = dcc.Dropdown(["Bubble Map", "Line Graph"], value = "Bubble Map",id = "graph-selector", className = "dropdown_cat", clearable=False)

# App layout, important to note are the dcc loading object, and the range slider that are new here
app.layout = html.Div(children= [
    dbc.Row(dbc.Col(html.H1(children = "Mobility data throughout a Pandemic", style = {"color": "#78c2ad", "padding": 5}),
                width={"size":6, "offset": 3})),
    dbc.Row(dbc.Col(html.H5(children= '''
    Please select a category of location, the year to base the country GDP colors on and the type of graph you would like to see''', style = {"color": "#f3969a", "padding": 5}),
                width={"size":5, "offset": 3})),
    dbc.Row([
        dbc.Col(category_dropdown, 
            width = {"size" : 2, "offset" : 3}),
        dbc.Col(date_dropdown, 
            width = {"size" : 2, "offset" : 0}),
        dbc.Col(graph_dropdown, 
            width = {"size" : 2, "offset" : 0})
        ]),
    dbc.Row(dbc.Col(html.H5(id="category-container", style = {"color": "#f3969a", "padding": 10}),
            width={"size":5, "offset": 3})),
    dbc.Row([dbc.Col(dcc.Loading(dcc.Graph(id='Map-category', figure = {}), type="cube", color = "#f3969a"),
            width = {"size": 10,"offset":1})]),
    dbc.Row(dbc.Col(dcc.RangeSlider(0,120000, value = [30000,70000], id = "ranger-slider"),
            width={"size" : 10, "offset" : 1}))  
])

@app.callback(
    [Output('category-container', 'children'),
    Output('Map-category', component_property= 'figure')],
    [Input('category-selector', 'value'),
    Input('date-selector', 'value'),
    Input('graph-selector', 'value'),
    Input('ranger-slider',"value")])


def update_output(value,selected_date,graph,GDPrange):
    # Text telling the user what the graph is currently representing 
    container = f"Currently looking at the {value_to_label[value]} data, with the world wide GPD per capita in {selected_date} for countries with a GDP per capita between {GDPrange[0]} USD and ${GDPrange[1]} USD"

    # Loading the needed data, and adding the GPD data
    f = pd.read_parquet("Averages all categories", columns = ["Country", "date", str(value)])
    df = pd.DataFrame(f)
    df['date'] = pd.to_datetime(df['date'], )
    df2 = df.groupby(["Country",pd.Grouper(freq="w",key = "date")]).mean()[value].reset_index()
    df2["GDP 2020"]= df2["Country"].map(dict2020)
    df2["GDP 2021"]= df2["Country"].map(dict2021)
    df2["GDP 2022"]= df2["Country"].map(dict2022)
    Final_df = df2.loc[(df2[f"GDP {selected_date}"] >= GDPrange[0]) & (df2[f"GDP {selected_date}"] <= GDPrange[1])]
    # Code of the bubble map
    if graph == "Bubble Map":
        fig = px.scatter_geo(Final_df, locations= "Country", locationmode= "country names",
                            hover_name="Country", size= value,
                            animation_frame=Final_df.date.astype(str),
                            hover_data = {"Country": True, f"GDP {selected_date}": True, value: False},
                            color = f"GDP {selected_date}", color_continuous_scale = ["#78c2ad","#f3969a"])
        fig.update_geos(
        visible=False, resolution=50, showland = True, landcolor = "#fff",
        showocean = True, oceancolor = backgroundcolor)
    # code for the line graph
    if graph == "Line Graph":
        fig = px.line(Final_df, x="date", y=value, color="Country", labels = {value: "Time spent compared to baseline (in percentages)"})

    # Styling code that both of the graphs would need
    fig.update_layout(paper_bgcolor = backgroundcolor, plot_bgcolor = backgroundcolor,
                    margin=dict(l=0, r=0, t=0, b=0), height = 650,
                    font_color = "#ffffff")

    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)


