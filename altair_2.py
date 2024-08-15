import streamlit as st
import pandas as pd
import altair as alt

Vendas = pd.DataFrame({
    'Month': ['01-Jan', '02-Feb', '03-Mar', '04-Apr', '05-Mai', 
    '06-Jun', '07-Jul', '08-Ago', '09-Set', '10-Oct', '11-Nov', 
    '12-Dec'],
    'product_A' : [28,55,43,91,81,53,19,87,52,85,101,77],
    'product_B' : [93,68,79,84,81,97,109,99,125,115,120,88]
})
Vendas

st.subheader('GRÁFICO DE LINHAS: PRODUTOS A & B')

graf_linha_A = alt.Chart(Vendas).mark_line(
    point=alt.OverlayMarkDef(color='red', size=100, filled=False, fill='white'),
    color='red'
).encode(
    x = alt.X('Month'),
    y = alt.Y('product_A',
    axis=alt.Axis(grid=False),
    scale=alt.Scale(domain=(0,160))),
    tooltip = ['Month','product_A','product_B'] 
).properties(
    width=600,
    height=300,
    title = 'VENDAS MENSAIS DOS PRODUTOS A & B'
)

graf_linha_B = alt.Chart(Vendas).mark_line(
    point=alt.OverlayMarkDef(color='green', size=100, filled=False, fill='white'),
    color='green'
).encode(
    x = alt.X('Month'),
    y = alt.Y('product_B'),
    tooltip = ['Month','product_A','product_B']
)

rotulo_A = graf_linha_A.mark_text(
    dy = -15,
    y = 14
).encode(
    text = 'product_A'
)

rotulo_B = graf_linha_B.mark_text(
    dy = -15,
    y = 14
).encode(
    text = 'product_B'
)


st.altair_chart(graf_linha_A+graf_linha_B+rotulo_A+rotulo_B)