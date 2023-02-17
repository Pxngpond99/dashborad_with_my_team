import pandas 
import plotly.express as px

df = pandas.read_excel("data_analize/data/dead_conso-3-54-65.xlsx")
df['Sex'] = df['Sex'].replace([0.0 , 1.0 , 2.0 , 3.0],['Not Specified' , 'Male','Female','Not Specified'])
df['Sex'] = df['Sex'].fillna('Not Specified')
quantity = df.groupby(['DEAD_YEAR(Budha)','Sex','Vehicle']).size().reset_index(name='counts')
male = quantity[quantity['Sex'] == 'Male']
female = quantity[quantity['Sex'] == 'Female']

fig = px.line(male, x="DEAD_YEAR(Budha)", y="counts", color="Vehicle",title="Male_Graph",template="plotly_dark")


fig2 = px.line(female, x="DEAD_YEAR(Budha)", y="counts", color="Vehicle",title="Female_Graph",template="plotly_dark")
