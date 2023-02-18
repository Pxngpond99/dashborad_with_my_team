import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df= pd.read_excel("data_analize/data/dead_conso-3-54-65.xlsx",usecols=['DEAD_YEAR(Budha)','Sex','Vehicle','Age','DeadDate','AccProv'])
df_map = pd.read_csv("data_analize/data/laclon.csv")
df = df[df["Age"] >= 1]

Age_Range = []
for row in df['Age']:
    if row >= 1.0 and row <= 3.0 :Age_Range.append('baby')
    elif row >= 4.0 and row <= 6.0 :Age_Range.append('child')
    elif row >= 7.0 and row <= 20.0 :Age_Range.append('teenage')
    elif row >= 21.0 and row <= 60.0 :Age_Range.append('worker')
    elif row >= 60.0 :Age_Range.append('elder')
df['Age_Range'] = Age_Range

df = df.dropna(subset=['DeadDate'])

df['DeadDate'] = df['DeadDate'].astype(str)
Month = []
for row in df['DeadDate']:
    if '-01-'  in row :Month.append('January')
    elif '-02-'  in row :Month.append('February')
    elif '-03-'  in row :Month.append('March')
    elif '-04-'  in row :Month.append('April')
    elif '-05-'  in row :Month.append('May')
    elif '-06-'  in row :Month.append('June')
    elif '-07-'  in row :Month.append('July')
    elif '-08-'  in row :Month.append('August')
    elif '-09-'  in row :Month.append('September')
    elif '-10-'  in row :Month.append('October')
    elif '-11-'  in row :Month.append('November')
    elif '-12-'  in row :Month.append('December')
df['Month'] = Month

df['Sex'] = df['Sex'].replace([0.0 , 1.0 , 2.0 , 3.0],['Not Specified' , 'Male','Female','Not Specified'])
df['Sex'] = df['Sex'].fillna('Not Specified')



quantity = df.groupby(['DEAD_YEAR(Budha)','Month','Sex']).size().reset_index(name='counts')
quantity_vehicle = df.groupby(['DEAD_YEAR(Budha)','Vehicle','Month']).size().reset_index(name='counts')
male = quantity[quantity['Sex'] == 'Male']
female = quantity[quantity['Sex'] == 'Female']


fig_line_month_sex = px.bar(quantity, 
                                x='Month', 
                                y="counts", 
                                color="Sex",
                                title="Graph",
                                template="plotly_dark",
                                )


age_with_acci = df.groupby(['Vehicle' , 'Age_Range']).size().reset_index(name='counts')
