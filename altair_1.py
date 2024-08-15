import altair as alt
import pandas as pd
import streamlit as st

fonte = pd.DataFrame({    
    'a' : ['A','B','C','D','E','F','G','H','I'],
    'b' : [28, 55, 43, 91, 81, 53, 19, 87, 52 ]
})

#Gráfico de barras 1
graf_barras = alt.Chart(fonte).mark_bar().encode(
    x = 'a',
    y = 'b',
    color = 'a',
    tooltip = ['a','b']
)
rotulo_barra = graf_barras.mark_text(
    dy = -8,
    size = 17
).encode(
    text='b',
    )
st.subheader('Plot do gráfico de barras :)')
st.altair_chart(graf_barras+rotulo_barra, use_container_width=True)

#Gráfico de barras 2
graf_barras_novo = alt.Chart(fonte).mark_bar(
    cornerRadiusTopLeft = 10,
    cornerRadiusTopRight = 10
).encode(
    x = alt.X('a', sort='y'),
    y = 'b',
    color = alt.condition(
        alt.datum.b > 43,
        alt.value('steelblue'),
        alt.value('black')
    )
)
rotulo_barra_novo = graf_barras_novo.mark_text(
    align = 'center',
    baseline = 'middle',
    size = 14,
    dy = -10
).encode(text = 'b')

linha_media = alt.Chart(fonte).mark_rule(color='red').encode(
    y='mean(b)'
)

st.subheader('Plot do novo gráfico de barras')
st.altair_chart(graf_barras_novo+rotulo_barra_novo+linha_media, use_container_width=True)

#Gráfico de Área
graf_area = alt.Chart(fonte).mark_area(
    color = 'lightblue',
    interpolate = 'step-after',
    line = True
).encode(
    x='a',
    y='b',
    tooltip = ['a','b']
)
rotulo_area = graf_area.mark_text(
    dy = -8,
    dx = 30,
    size = 17
).encode(
    text='b',
    )
st.subheader("Gráfico de área")
st.altair_chart(graf_area+rotulo_area, use_container_width=True)

#Gráfico de Pizza
graf_pizza = alt.Chart(fonte).mark_arc().encode(
    theta = alt.Theta(field='b', type = 'quantitative'),
    color = alt.Color(field='a', type='nominal'),
)
st.altair_chart(graf_pizza)
