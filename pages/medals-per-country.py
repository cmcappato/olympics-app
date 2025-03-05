import streamlit as st
import pandas as pd

st.set_page_config(page_title="Medals per country")
st.title("Análisis de Medallas")

if "OlympicsData" in st.session_state:
    oly = st.session_state["OlympicsData"]
    st.write("Datos cargados exitosamente.")
    if "CountryCodesData" in st.session_state:
        countries = st.session_state["CountryCodesData"]
        st.write("Datos cargados exitosamente.")
    else:
        st.error("Los datos aún no han sido cargados. Vuelve a la página principal.")
else:
    st.error("Los datos aún no han sido cargados. Vuelve a la página principal.")


def medals_per_country(df):
    medals_count = df[df['Medal'].isin(['Gold', 'Silver', 'Bronze'])]

    medals_per_country = medals_count.pivot_table(index='IOC', 
                                columns='Medal', 
                                aggfunc='size', 
                                fill_value=0)
    
    for column in ['Gold', 'Silver', 'Bronze']:
        if column not in medals_per_country:
            medals_per_country[column] = 0 
    
    return medals_per_country


def change_ioc_for_country(country_df, oly_df):
    countries_new = oly_df.merge(country_df[["IOC","CountryName"]], on="IOC", how="left")
    print(countries_new)
    countries_new = countries_new.drop(columns=["IOC"])

    return countries_new




show_medals = medals_per_country(oly)
change_ioc = change_ioc_for_country(countries, show_medals)


st.dataframe(change_ioc, 
            column_order=['CountryName', 'Gold', 'Silver', 'Bronze'],
            width=500)
