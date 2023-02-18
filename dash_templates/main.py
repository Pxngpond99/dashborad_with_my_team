from app_layout import *
from dash import Input, Output
import pandas
@app.callback(Output("pie-graph", "figure"), Input('dd-output-container', "value"))
def show_data(selected_year):
    df_each_year = df[df['DEAD_YEAR(Budha)'] == selected_year]

    fig_pie_age_range = px.pie(
        df_each_year['Age_Range'],
        names='Age_Range',
        title="Accident mortality rate by age group in {}".format(selected_year),
        template="plotly_dark"
    )
    return fig_pie_age_range

@app.callback(Output("sex-bar-graph", "figure"), Input('dd-output-container', "value"))
def show_data(selected_year):
    df_each_year = quantity[quantity['DEAD_YEAR(Budha)'] == selected_year]
    
    fig_bar_month_sex = px.bar(df_each_year, 
                                x="Month", 
                                y="counts", 
                                color="Sex",
                                title="Gender and accident mortality rates in {}".format(selected_year),
                                template="plotly_dark",
                                )
    fig_bar_month_sex.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [1,2,3,4,5,6,7,8,9,10,11,12],
        ticktext = ['January', 'February', 'March', 'April','May','June','July','August','September','October','November','December']
    )
)
    return fig_bar_month_sex

@app.callback(Output("vehicle-bar-graph", "figure"), Input('dd-output-container', "value"))
def show_data(selected_year):
    df_each_year = age_with_acci[age_with_acci['DEAD_YEAR(Budha)'] == selected_year]
    
    fig_bar_month_vehicle = px.bar(df_each_year, 
                                x="Vehicle", 
                                y="counts", 
                                color="Age_Range",
                                title="Death rate from vehicle accidents of each month in {}".format(selected_year),
                                template="plotly_dark",
                                )
    return fig_bar_month_vehicle

@app.callback(Output("line-graph", "figure"), Input('dd-output-container', "value"))
def show_data(selected_year):
    df_each_year = quantity_vehicle[quantity_vehicle['DEAD_YEAR(Budha)'] == selected_year]
    fig_line_month_sex = px.line(df_each_year, 
                                x="Month", 
                                y="counts", 
                                color="Vehicle",
                                title="Accidental mortality rate for each month in {}".format(selected_year),
                                template="plotly_dark",
    )
    fig_line_month_sex.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [1,2,3,4,5,6,7,8,9,10,11,12],
        ticktext = ['January', 'February', 'March', 'April','May','June','July','August','September','October','November','December']
    )
)
    return fig_line_month_sex

if __name__ == "__main__":
    app.run_server(debug=True)