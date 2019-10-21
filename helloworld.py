import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

df = st.cache(pd.read_csv)("football_data.csv")

clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.sidebar.multiselect('Show Player from Nationalities?', df['Nationality'].unique())

new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
st.write(new_df)

fig = px.scatter(new_df, x ='Overall',y='Age',color='Name')

st.plotly_chart(fig)
