from app_layout import *
from dash import Input, Output

@app.callback(Output("pie-graph", "figure"), Input('dd-output-container', "value"))
def show_data(selected_year):
    df_each_year = df[df['DEAD_YEAR(Budha)'] == selected_year]

    fig_pie_age_range = px.pie(
        df_each_year['Age_Range'],
        names='Age_Range',
        title="Pie Graph About Age Range In{}".format(selected_year)
    )
    return fig_pie_age_range

@app.callback(Output("line-graph", "figure"), Input('dd-output-container', "value"))
def show_data(selected_year):
    df_each_year = df[df['DEAD_YEAR(Budha)'] == selected_year]
    fig_line_month_sex = px.bar(df_each_year, 
                                x="Month", 
                                y="counts", 
                                color="Sex",
                                title="Graph",
                                template="plotly_dark")
    
    return fig_line_month_sex

if __name__ == "__main__":
    app.run_server(debug=True)