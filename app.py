import pandas as pd
import scipy.stats
from scipy.stats import rv_discrete
import streamlit as st
import time

# estas son variables de estado que se conservan cuando Streamlin vuelve a ejecutar este script
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar un dado')
st.write("Se lanza un dado y se grafican los resulatados por cada set de tiradas. Se almanecan los sets independientes en una tabla")
st.write("omaiga. Sí pudimos")


chart = st.line_chart([0.5])

def roll_dice(n):
    # Valores y probabilidades de un dado justo
    valores = [1, 2, 3, 4, 5, 6]
    probabilidades = [1/6] * 6

    # Crear la distribución discreta para el dado
    dado = rv_discrete(name='dado', values=(valores, probabilidades))

    # Generar los resultados de los lanzamientos
    trial_outcomes = dado.rvs(size=n)

    mean = None
    outcome_no = 0
    total_sum = 0

    for r in trial_outcomes:
        outcome_no += 1
        total_sum += r
        mean = total_sum / outcome_no
        # Aquí asumimos que chart es un objeto de visualización para graficar resultados
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 50)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    mean = roll_dice(number_of_trials)
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            mean]],
                    columns=['no', 'iteraciones', 'media'])
        ],
        axis=0)
    st.session_state['df_experiment_results'] = st.session_state['df_experiment_results'].reset_index(drop=True)

st.write(st.session_state['df_experiment_results'])