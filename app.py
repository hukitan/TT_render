#preambulo importamos paquetes a usar
import streamlit as st
import pandas as pd
import plotly.express as px
import lib 


def wide_space_default():
    st.set_page_config(layout="wide")
wide_space_default()

#Preambulo de datos
url1 = "https://datos.cdmx.gob.mx/dataset/f2046fd5-51b5-4876-b008-bd65d95f9a02/resource/cce544e1-dc6b-42b4-bc27-0d8e6eb3ed72/download/afluenciastc_desglosado_10_2024.csv"
url2 = "https://datos.cdmx.gob.mx/dataset/f2046fd5-51b5-4876-b008-bd65d95f9a02/resource/0e8ffe58-28bb-4dde-afcd-e5f5b4de4ccb/download/afluenciastc_simple_02_2024.csv"

aflue1 = pd.read_csv(url1)
aflue2 = pd.read_csv(url2)

aflue = pd.concat([aflue1, aflue2])
aflue["fecha"] = pd.to_datetime(aflue["fecha"])
aflue["n_mes"] = aflue["fecha"].dt.month
aflue["linea"] = aflue["linea"].apply(lib.fix_linea)
aflue["mes"] = aflue["n_mes"].apply(lib.fill_mes)
# Se generan codigos de color para poder usar los colores oficiales por linea del metro
colores = {"Linea 1": "#F04E98", "Linea 2": "#005EB8", "Linea 3": "#AF9800", "Linea 4": "#6BBBAE", "Linea 5": "#FFD100", "Linea 6": "#DA291C",
           "Linea 7": "#E87722", "Linea 8": "#009A44", "Linea 9": "#512F2E", "Linea A": "#981D97", "Linea B": "#B1B3B3", "Linea 12": "#B0A32A"}

#Body
st.header("Datos historicos del metro de la CDMX")
st.write("Se usan los datos oficiales del gobierno de la Ciudad de México")

hist_button = st.button('Construir histograma')
disp_button = st.button('Construir diagrama de dispersion')
# crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma con los datos de la afluencia para los años de 2021 a 2024')

    # crear un histograma
    graf1d = aflue.pivot_table(index=["anio", "mes"], values="afluencia", aggfunc="sum").reset_index()
    fig = px.histogram(graf1d, x="afluencia", color="anio",title="Afluencia agrupada por año")  # crear un histograma
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

elif disp_button:
    st.write('Creación de un diagrama de dispersion para la afluencia de los años 2021 a 2024, separado por linea y utilizando los colores oficiales del Metro CDMX')
    #Datos para la generacion del grafico
    graf2d = aflue.pivot_table(
        index=["anio", "mes", "linea"], columns="tipo_pago", values="afluencia", aggfunc="sum").reset_index()
    graf2d["de_pago"] = graf2d["Boleto"] + graf2d["Prepago"]
    graf2d = graf2d.drop(columns=['Boleto', "Prepago"])
    #Grafico de dispersion
    fig = px.scatter(graf2d, x="de_pago", y="Gratuidad", color="linea", color_discrete_map=colores,
                    title="Afluencia total: Usuarios que pagan vs Usuarios gratuitos (color por linea)")
    fig.update_layout(
        xaxis_title="Usuarios que pagan",
        yaxis_title="Usuarios gratuitos")
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
