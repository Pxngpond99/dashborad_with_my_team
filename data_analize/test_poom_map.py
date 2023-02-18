from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import geopandas as gpd
import shapely
import matplotlib.pyplot as plt
import plotly.graph_objs as go
app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])

colors = {"background": "#111111", "text": "#7FDBFF"}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df= pd.read_excel("dashborad_with_my_team\data_analize\data\dead_conso-3-54-65.xlsx",usecols=['DEAD_YEAR(Budha)','Sex','Vehicle','Age','DeadDate','AccProv'])
df_1 = df[df["Age"] >= 1]
df_2 = df_1.dropna(subset=['DeadDate'])
df_2['AccProv'] = df_2['AccProv'].replace('ไม่ทราบจังหวัด','กรุงเทพมหานคร')
map = df_2.groupby(['DEAD_YEAR(Budha)','AccProv']).size().reset_index(name='counts')
map_1 = map[map["DEAD_YEAR(Budha)"] == 2554]


# quantity = df.groupby(['DEAD_YEAR(Budha)','Sex','Vehicle']).size().reset_index(name='counts')
# df.columns = [
#     "BE",
#     "emission_type",
#     "category",
#     "sub_category",
#     "en_sub_category",
#     "quantity",
# 
# male = quantity[quantity['Sex'] == 1.0]
# female = quantity[quantity['Sex'] == 2.0]

df_lac = pd.read_csv("dashborad_with_my_team\data_analize\data\laclon.csv")
count_c = []
num = []
for x in [i for i in df_lac['ชื่อ']]:
    for y in [j for j in map_1['AccProv']]:
        
        if x == y:
            num = map_1.index[map_1['AccProv']==y].tolist()
            count_c.append(map_1['counts'][num[0]])
df_lac1 = df_lac
df_lac1['count_c'] = count_c




# initialize an axis
# fig, ax = plt.subplots(figsize=(8,6))
# # plot map on axis
# countries = gpd.read_file(  
#      gpd.datasets.get_path("naturalearth_lowres"))
# countries[countries["name"] == "Thailand"].plot(color="lightgrey",
#                                                  ax=ax)
# # plot points
# df.plot(x="lon", y="lac", kind="scatter", ax=ax)
# layout = go.Layout(
#     geo = dict(
#         center = dict(lon=-0.1262, lat=51.5074), # set the center to London
#         scope = "world",
#         projection_type = "equirectangular",
#         zoom = 3 # set the zoom level to 3
#     )
# )

# fig3 = go.Figure(data=df, layout=layout)

fig3 = px.scatter_geo(df_lac1,lat="lac",lon="lon",scope="asia",center=dict(lat=14.52892, lon=100.9101),hover_name="count_c",text="ขื่อ")       



# fig = px.line(male, x="DEAD_YEAR(Budha)", y="counts", color="Vehicle",title="Male_Graph")


# fig2 = px.line(female, x="DEAD_YEAR(Budha)", y="counts", color="Vehicle",title="Female_Graph")



app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Hello Dash",
                    style={
                        "textAlign": "center",
                    },
                )
            ],
            className="row",
        ),
        html.Div(
            children=[
                html.Div(
                    children="Dash: A web application framework for your data.",
                    style={
                        "textAlign": "center",
                    },
                ),
            ],
            className="row",
        ),
        html.Div(
            children=[
                html.Div(
                    [dcc.Graph(id="example-graph-1", figure=fig3)], className="col"
                ),
                html.Div(
                    [dcc.Graph(id="example-graph-2", figure=fig3)], className="col"
                ),
            ],
            className="row",
        ),
        html.Div([
            html.Button("Hello", className="btn btn-primary")
        ],className="row",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
