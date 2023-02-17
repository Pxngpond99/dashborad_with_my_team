import dash_bootstrap_components as dbc
from dash import Dash, dcc,html ,Input, Output
from data_file import *
app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])


# @app.callback(Output("pie-graph", "figure"), Input("year-slider", "value"))
# def show_data(selected_year):
#     filtered_df = quantity[quantity.DEAD_YEAR == selected_year]

#     fig = px.pie(
#         filtered_df,
#         values="Vehicle",
#         names=male,
#         color=male,
#         title="Pie Graph About Energy Sector",
#     )
#     return fig

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
        # html.Div(
        #             [
        #                 dcc.Graph(id="pie-graph"),

        #             ],
        #             # className="col-6",
        #         ),
        # html.Div(
        #             [
        #                 dcc.Slider(
        #                     df["DEAD_YEAR"].min(),
        #                     df["DEAD_YEAR"].max(),
        #                     step=None,
        #                     value=df["DEAD_YEAR"].min(),
        #                     marks={str(year): str(year) for year in df["DEAD_YEAR"].unique()},
        #                     id="year-slider",
        #                 ),
        #             ],
        #             style={"padding-top": "20px;"},
        #             # className="col-sm",
        #         ),
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
