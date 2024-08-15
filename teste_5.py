import streamlit as st
import pandas as pd
import numpy as np

st.subheader('Exemplo 6 - Temperatura')
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "25 °C", "2 °C")
col2.metric("Vento", "10 km/h", "-8%")
col3.metric("Humidade", "86%", "4%", delta_color="inverse")