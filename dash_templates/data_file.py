import pandas 
import plotly.express as px

df = pandas.read_excel("data_analize/data/dead_conso-3-54-65.xlsx")



df['Sex'] = df['Sex'].replace([0.0 , 1.0 , 2.0 , 3.0],['Not Specified' , 'Male','Female','Not Specified'])
df['Sex'] = df['Sex'].fillna('Not Specified')
quantity = df.groupby(['DEAD_YEAR(Budha)','Sex','Vehicle']).size().reset_index(name='counts')
male = quantity[quantity['Sex'] == 'Male']
female = quantity[quantity['Sex'] == 'Female']



fig1 = px.line(male, x="DEAD_YEAR(Budha)", y="counts", color="Vehicle",title="Male_Graph",template="plotly_dark")
Age_Range = []
df = df[df["Age"] >= 1]
for row in df['Age']:
    if row >= 1.0 and row <= 3.0 :Age_Range.append('baby')
    elif row >= 4.0 and row <= 6.0 :Age_Range.append('child')
    elif row >= 7.0 and row <= 20.0 :Age_Range.append('teenage')
    elif row >= 21.0 and row <= 60.0 :Age_Range.append('worker')
    elif row >= 60.0 :Age_Range.append('elder')
df['Age_Range'] = Age_Range

age_with_acci = df.groupby(['Vehicle' , 'Age_Range']).size().reset_index(name='counts')
fig2 = px.line(female, x="DEAD_YEAR(Budha)", y="counts", color="Vehicle",title="Female_Graph",template="plotly_dark")

fig = px.pie(df['Age_Range'],
        names='Age_Range',
        title="Pie Graph About Vehicle")
