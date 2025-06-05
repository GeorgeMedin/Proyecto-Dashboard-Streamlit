import streamlit as st
import pandas as pd

titulo = "Datos de transmisión global de Spotify"
icono = "🎵"

# Metadatos del dashboard
st.set_page_config(
    page_title=titulo,
    page_icon=icono,
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.header(titulo + icono + icono)

# Cargar base de datos
BaseData = pd.read_csv("baseDatos/SpotifyBD.csv")

BaseData.columns = ["Pais", "Artista", "Album", "Genero", "Ano", "Oyentes Mes", "Total Trasmitida", "Horas Trasmitida", "Prom. Duracion", "Tipo Plataforma", "Trasmision 30 días", "Tasa de Cambio"]

# Inicializar estado
if "filterYear" not in st.session_state:
    st.session_state.filterYear = "Todos"
if "filterCountry" not in st.session_state:
    st.session_state.filterCountry = []  # Ya no tiene "Todos"

# Función para resetear filtros
def resetFilters():
    st.session_state.filterYear = "Todos"
    st.session_state.filterCountry = []

# Sidebar
with st.sidebar:
    if st.button("Quitar Filtros ✖", key="reset_button"):
        resetFilters()

    st.selectbox(
        "Año", 
        options=["Todos"] + sorted(BaseData['Ano'].unique().tolist()), 
        index=0 if st.session_state.filterYear == "Todos" else (sorted(BaseData['Ano'].unique().tolist()).index(st.session_state.filterYear) + 1),
        key="filterYear"
    )

    st.multiselect(
        "Pais", 
        options=sorted(BaseData['Pais'].unique()),
        default=st.session_state.filterCountry,
        key="filterCountry"
    )

# Filtrar datos
dataFiltrada = BaseData.copy()

if st.session_state.filterYear != "Todos":
    dataFiltrada = dataFiltrada[dataFiltrada['Ano'] == st.session_state.filterYear]

if len(st.session_state.filterCountry) > 0:
    dataFiltrada = dataFiltrada[dataFiltrada['Pais'].isin(st.session_state.filterCountry)]

# Mostrar resultado
st.dataframe(dataFiltrada)
