from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas
import plotly.graph_objects as go
app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])

colors = {"background": "#111111", "text": "#7FDBFF"}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pandas.read_excel("dashborad_with_my_team\data\dead_conso-3-54-65.xlsx")
quantity = df.groupby(['DEAD_YEAR(Budha)','Sex','Vehicle']).size().reset_index(name='counts')
df_map = pandas.read_csv("data_analize/data/laclon.csv")
# df.columns = [
#     "BE",
#     "emission_type",
#     "category",
#     "sub_category",
#     "en_sub_category",
#     "quantity",
# 
male = quantity[quantity['Sex'] == 1.0]
female = quantity[quantity['Sex'] == 2.0]


df['AccProv'] = df['AccProv'].replace('ไม่ทราบจังหวัด','กรุงเทพมหานคร')
map = df.groupby(['AccProv']).size().reset_index(name='counts')
ColorMap = []
for row in map['counts']:
    if row > 0 and row < 500  :ColorMap.append('green')
    elif row >= 500 and row < 1000 :ColorMap.append('yellow')
    elif row >= 1000  :ColorMap.append('red')
map['ColorMap'] = ColorMap

fig_map = go.Figure(data=go.Scattergeo(
        lon = df_map['lon'],
        lat = df_map['lac'],
        text = df_map['ชื่อ'],
        mode = 'markers',
        marker_color = map['ColorMap'],
        ))

fig_map.update_layout(
        title = 'Thailand',
        geo_scope='asia',
    )
fig = px.line(male, x="DEAD_YEAR(Budha)", y="counts", color="Vehicle",title="Male_Graph")


fig2 = px.line(female, x="DEAD_YEAR(Budha)", y="counts", color="Vehicle",title="Female_Graph")

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
                    [dcc.Graph(id="example-graph-1", figure=fig)], className="col"
                ),
                html.Div(
                    [dcc.Graph(id="example-graph-2", figure=fig2)], className="col"
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



