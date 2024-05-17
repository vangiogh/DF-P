import pandas as pd
import streamlit as st
import plotly.express as px

df_base = pd.read_csv('data/gapminder.csv')

options_year = df_base['year'].unique()
value_year = st.selectbox('Year', options_year)
mask_year = df_base['year'] == value_year

df = df_base[mask_year]
df

fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent', hover_name='country', log_x=True)
fig