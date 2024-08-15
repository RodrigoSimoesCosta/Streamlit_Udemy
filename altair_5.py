import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv('./Datasets/vega_car.csv')
df

disper1 = alt.Chart(df).mark_point().encode(
    x = 'Horsepower:Q',
    y = 'Miles_per_Gallon',
    color = alt.Color('Origin:N')

)

st.subheader('GRÁFICO DE DISPERSÃO 1')

st.altair_chart(disper1, use_container_width=True)

disper2 = alt.Chart(df).mark_point().encode(
    x = 'Weight_in_lbs:Q',
    y = 'Miles_per_Gallon',
    color = alt.Color('Origin:N')

)

st.subheader('GRÁFICO DE DISPERSÃO 2')

st.altair_chart(disper2, use_container_width=True)