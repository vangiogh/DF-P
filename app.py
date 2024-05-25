import pandas as pd
import streamlit as st
import plotly.express as px

df_rich = pd.read_excel('data/richest_clean.xlsx')

pd_unique = df_rich['Industry'].unique().tolist()
pd_unique.sort(reverse=False)

industry = st.sidebar.selectbox(label='Seleccione una de las opciones', options=pd_unique)

mask_industry = df_rich['Industry'] == industry
df_industry = df_rich[mask_industry]

df_industry = df_industry.sort_values('Total Net Worth')

fig = px.bar(data_frame=df_industry, x='Total Net Worth', y='Name')
fig