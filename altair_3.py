import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_excel(
    io = './Datasets/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name = 'flow',
    usecols = 'A:B',
    nrows = 15,
)

graf_area = alt.Chart(df).mark_area(
    color = 'gray',
    line = {'color':'black'}
).encode(
    x = 'Year:T', 
    y = 'Value:Q'
)

rotulo = graf_area.mark_text(
    size = 14,
    color = 'black',
    align = 'center',
    dy = -15
).encode(text='Value')

st.subheader('KPI DE RESULTADOS ANUAIS')
st.altair_chart(graf_area+rotulo, use_container_width = True)
