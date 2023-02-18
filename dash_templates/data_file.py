import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df= pd.read_excel("data_analize/data/dead_conso-3-54-65.xlsx",usecols=['DEAD_YEAR(Budha)','Sex','Vehicle','Age','DeadDate','AccProv'])
df_map = pd.read_csv("data_analize/data/laclon.csv")

df = df[df["Age"] >= 1]

Age_Range = []
for row in df['Age']:
    if row >= 0.0 and row <= 3.0 :Age_Range.append('Baby : 0-3 y')
    elif row >= 4.0 and row <= 6.0 :Age_Range.append('Child : 4-6 y')
    elif row >= 7.0 and row <= 20.0 :Age_Range.append('Teenage : 7-20 y')
    elif row >= 21.0 and row <= 60.0 :Age_Range.append('Worker : 21-60 y')
    elif row > 60.0 :Age_Range.append('Elder : 60+ y')
df['Age_Range'] = Age_Range

df = df.dropna(subset=['DeadDate'])

df['DeadDate'] = df['DeadDate'].astype(str)
Month = []
for row in df['DeadDate']:
    if '-01-'  in row :Month.append(1)
    elif '-02-'  in row :Month.append(2)
    elif '-03-'  in row :Month.append(3)
    elif '-04-'  in row :Month.append(4)
    elif '-05-'  in row :Month.append(5)
    elif '-06-'  in row :Month.append(6)
    elif '-07-'  in row :Month.append(7)
    elif '-08-'  in row :Month.append(8)
    elif '-09-'  in row :Month.append(9)
    elif '-10-'  in row :Month.append(10)
    elif '-11-'  in row :Month.append(11)
    elif '-12-'  in row :Month.append(12)
df['Month'] = Month

df['Sex'] = df['Sex'].replace([0.0 , 1.0 , 2.0 , 3.0],['Not Specified' , 'Male','Female','Not Specified'])
df['Sex'] = df['Sex'].fillna('Not Specified')


quantity = df.groupby(['DEAD_YEAR(Budha)','Month','Sex']).size().reset_index(name='counts')
quantity_vehicle = df.groupby(['DEAD_YEAR(Budha)','Vehicle','Month']).size().reset_index(name='counts')
age_with_acci = df.groupby(['DEAD_YEAR(Budha)','Vehicle' , 'Age_Range']).size().reset_index(name='counts')

map_1 = df.groupby(['DEAD_YEAR(Budha)','AccProv']).size().reset_index(name='counts')
