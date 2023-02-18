import dash_bootstrap_components as dbc
from dash import Dash, dcc,html
from data_file import *
app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

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
                    [
                        dcc.Graph(id="pie-graph"),
                        dcc.Graph(id="line-graph"),
                        html.Div(
                    [dcc.Graph(id="example-graph-2", figure=fig_line_month_sex)],
                    [dcc.Graph(id="example-graph-3", figure=fig_line_month_sex)],className="col"
                ),
                    ],
                    className="col-6",
                ),
        html.Div(
                    [
                        dcc.Slider(
                            df["DEAD_YEAR(Budha)"].min(),
                            df["DEAD_YEAR(Budha)"].max(),
                            step=None,
                            value=df["DEAD_YEAR(Budha)"].min(),
                            marks={str(year): str(year) for year in df["DEAD_YEAR(Budha)"].unique()},
                            id="year-slider",
                        ),
                    ],
                    style={"padding-top": "20px;"},
                    className="col-sm",
                ),
        html.Div(
                    [
                        dcc.Dropdown(
                            options=[x for x in df["DEAD_YEAR(Budha)"].unique()],
                            value=df["DEAD_YEAR(Budha)"].min(),
                            id='dd-output-container',
                        )
                    ],
                    style={"padding-top": "20px;"},
                    className="col-sm",
                    
                ),
        # html.Div(
        #     children=[
        #         html.Div(
        #             [dcc.Graph(id="example-graph-1", figure=fig)], className="col"
        #         ),
        #         html.Div(
        #             [dcc.Graph(id="example-graph-2", figure=fig2)], className="col"
        #         ),
        #     ],
        #     className="row",
        # ),
        html.Div([
            html.Button("Hello", className="btn btn-primary")
        ],className="row",
        ),
        
    ]
)
