import pandas as pd
import streamlit as st
import plotly.express as px

df_base = pd.read_excel('data/gapminder.xlsx')

options_year = df_base['year'].unique()
options_lifeExp = df_base['lifeExp'].agg(['min','max']).tolist()

with st.sidebar:
    value_year = st.selectbox('Year', options_year)
    value_lifeExp = st.slider('Life Expectancy', *options_lifeExp, options_lifeExp)
    
mask_year = df_base['year'] == value_year
mask_lifeExp = df_base['lifeExp'].between(*value_lifeExp)

df = df_base[mask_year & mask_lifeExp]

fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country', log_x=True)

st.title('Gapminder Data')

fig
df
