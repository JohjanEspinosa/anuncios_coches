import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

st.header("Análisis Exploratorio Anuncios de Coches")

# Botón Histograma
if st.button("Crear Histograma"):
    st.write("Creando histograma... 'odometer'")
    if 'odometer' in df.columns:
        fig = px.histogram(df, x='odometer', title='Histograma de Kilometraje de Coches')
    else:
        fig = px.histogram(df, x=df.columns[0], title='Histograma de {df.columns[0]}')
    st.plotly_chart(fig, use_container_width=True)
    
    # Botón gráfico de dispersión
if st.checkbox("Crear Gráfico de Dispersión"):
    st.write("Creando gráfico de dispersión... 'odometer' vs 'price'")
    if 'odometer' in df.columns and 'price' in df.columns:
        fig2 = px.scatter(df, x='odometer', y='price', title='Gráfico de Dispersión de Kilometraje vs Precio')
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.write("No se pueden crear gráficos de dispersión sin las columnas 'odometer' y 'price'")