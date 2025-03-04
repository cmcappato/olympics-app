import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from menu import menu

# Cargar datos
oly = pd.read_csv("csv-files/olympics-data-clean.csv")

# Filtrar solo los medallistas (descartar valores nulos en 'Medal')
df_medals = oly[oly['Medal'].notna()]

st.title("Visualización de Datos Olímpicos 🏅")

# Crear menú en la barra lateral
menu = st.sidebar.radio("Selecciona una visualización", 
                        ["Medallas por país", "Medallas por género", "Medallas por deporte"])

# Medallas por país
if menu == "Medallas por país":
    top_countries = df_medals['CountryName'].value_counts().head(10)
    fig1 = px.bar(x=top_countries.index, 
                y=top_countries.values, 
                title="Top 10 países con más medallas",
                labels={'x': 'País', 'y': 'Número de Medallas'},
                color=top_countries.index, 
                color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig1)

# Medallas por género
elif menu == "Medallas por género":
    gender_counts = df_medals['Gender'].value_counts()
    fig2, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', 
        colors=['#1f77b4', '#ff69b4'])  # Azul y rosa
    ax.set_title("Distribución de Medallas por Género")
    st.pyplot(fig2)

# Medallas por deporte
elif menu == "Medallas por deporte":
    top_sports = df_medals['Sport'].value_counts().head(10)
    fig3 = px.bar(x=top_sports.index, 
                y=top_sports.values, 
                title="Top 10 deportes con más medallas",
                labels={'x': 'Deporte', 'y': 'Número de Medallas'},
                color=top_sports.index, 
                color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig3)
