import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
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
