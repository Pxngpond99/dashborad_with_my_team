import dash_bootstrap_components as dbc
from dash import Dash, dcc,html ,dash_table
from data_file import *
app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Statistics of Road Traffic Fatalities in 2554-2565",
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
                    children="Select years for view data",
                    style={
                        "textAlign": "center","margin":"10px"
                    },
                ), html.Div(
                    [
                        dcc.Dropdown(
                            options=[x for x in df["DEAD_YEAR(Budha)"].unique()],
                            value=df["DEAD_YEAR(Budha)"].min(),
                            id='dd-output-container',
                        ),
                    ],
                    style={"top": "20px;","margin": "0 30vw 10px 30vw",},
                    className="col-sm",
                ),
            ],
            className="row",
        ),
        html.Div(
            children=[
                html.Div(
                    [dcc.Graph(id="line-graph"),], className="col-6"
                ),
                html.Div(
                    [dcc.Graph(id="vehicle-bar-graph")], className="col-6"
                ),
            ],style={
                         "margin":"10px "
                    },
            className="row",
        ),
        html.Div(
            children=[
                html.Div(
                    [dcc.Graph(id="pie-graph"),], className="col-6"
                ),
                html.Div(
                    [dcc.Graph(id="sex-bar-graph"),], className="col-6"
                ),
            ],style={
                         "margin":"10px "
                    },
            className="row",
        ),
        # html.Div(
        #             [
        #                 dcc.Slider(
        #                     df["DEAD_YEAR(Budha)"].min(),
        #                     df["DEAD_YEAR(Budha)"].max(),
        #                     step=None,
        #                     value=df["DEAD_YEAR(Budha)"].min(),
        #                     marks={str(year): str(year) for year in df["DEAD_YEAR(Budha)"].unique()},
        #                     id="year-slider",
        #                 ),
        #             ],
        #             style={"padding-top": "20px;"},
        #             className="col-sm",
        #         ),
        
    
        html.Div(children=[
                html.Div(
                    [dcc.Graph(id="Map-graph"),],className="col-6",style={
                         "margin":"10px 24vw "
                    },
                ),
                

            ],
        ),
        
    ]
)
