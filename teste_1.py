import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write("Este é um texto")


st.write(pd.DataFrame({
    'Coluna A': [1,2,3,4,5],
    'Coluna B': ["Cachorro", "Gato", "Cavalo", "Vaca", "Zebra"],
}))

array = [1, 2, "abc", "Martin", True]
st.write('Aqui temos uma array', array)


df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a','b','c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size = 'c', color='c', tooltip = ['a','b','c'])

st.write(df)
st.write(c)
