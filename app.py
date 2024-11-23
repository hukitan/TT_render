#preambulo importamos paquetes a usar
import streamlit as st
import pandas as pd
import plotly.express as px
import lib 

#Preambulo de datos
aflue = pd.read_csv("Data/afluenciastc_desglosado_10_2024.csv")
aflue["fecha"] = pd.to_datetime(aflue["fecha"])
aflue["n_mes"] = aflue["fecha"].dt.month
aflue["linea"] = aflue["linea"].apply(lib.fix_linea)
aflue["mes"] = aflue["n_mes"].apply(lib.fill_mes)
# Se generan codigos de color para poder usar los colores oficiales por linea del metro
colores = {"Linea 1": "#F04E98", "Linea 2": "#005EB8", "Linea 3": "#AF9800", "Linea 4": "#6BBBAE", "Linea 5": "#FFD100", "Linea 6": "#DA291C",
           "Linea 7": "#E87722", "Linea 8": "#009A44", "Linea 9": "#512F2E", "Linea A": "#981D97", "Linea B": "#B1B3B3", "Linea 12": "#B0A32A"}


st.header("Datos historicos del metro de la CDMX")
st.write("Se usan los datos oficiales del gobierno de la Ciudad de México")

