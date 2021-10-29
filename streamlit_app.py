import streamlit as st
from streamlit_folium import folium_static
import folium
from branca.element import Figure
import pandas as pd
import joblib
import geopandas as gpd
import folium.plugins as plugins
from folium.plugins import HeatMap
import numpy as np
from folium.plugins import MiniMap
from folium.plugins import MeasureControl
from PIL import Image
import plotly.express as px
import streamlit.components.v1 as components
import requests
import gc


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


icon = Image.open("icone.png")

st.set_page_config(
    page_title="Maos por Patas",
    layout='wide',
    initial_sidebar_state='auto',
    page_icon=icon
)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.sidebar.subheader('Menu')

study = st.sidebar.radio("ir para", ('Quem Somos', 'Informações de Animais',
                         'Informações de Casas de Ração'))

st.sidebar.write("---")

if study == 'Quem Somos':
    t1, mid, t2 = st.columns([20, 1, 10])
    with t1:
        st.markdown('# Movimento Mãos por Patas')

    with t2:
        # use_column_width=True)
        st.image(Image.open("vira-lata-caramelo.jpg"), width=200)

    st.write(
        """
        """)

    st.write(
        """
        O crime de abandono de animais é constante e tem se tornado algo maior, o grupo antes mesmo do Projeto Integrador já conhecia a ONG Animais de Rua Itapecerica da Serra e sempre apoiou o Movimento, estando desde sempre nesta luta para sanar a fome e sede animal, porém a falta de recurso e reconhecimento, são os principais motivos que os impossibilita de realmente traçar o objetivo final, vendo isso, para ajudar o Movimento de alguma forma decidimos criar um portal onde estará disponível adoção de animais, parceria entre casas de ração e também a divulgação do seu trabalho.
        """)

    st.markdown('### Parcerias')

    st.write(
        """
        Esse site foi desenvolvido como parte de Projeto Integrador da UNIVESP""")    

elif study == 'Informações de Animais':
    # functions end here, title, sidebar setting and descriptions start here
    t1, mid, t2 = st.columns([20, 1, 10])
    with t1:
        st.markdown('# Movimento Mãos por Patas')

    with t2:
        # use_column_width=True)
        st.image(Image.open("vira-lata-caramelo.jpg"), width=200)

    st.write(
        """
        O objetivo desse site é permitir uma análise mais detalhada sobre
        """)

    with st.expander("Expanda para cadastro de animais"):
        st.markdown('### ORIGEM DOS ')

elif study == 'Informações de Casas de Ração':

    t1, mid, t2 = st.columns([20, 1, 10])
    with t1:
        st.markdown('# Movimento Mãos por Patas')

    with t2:
        # use_column_width=True)
        st.image(Image.open("vira-lata-caramelo.jpg"), width=200)

    st.write(
        """
        O objetivo desse site é entender o posicionamento atual dos centros de distribuição alinhado com modelos de machine learning com propostas de localizações baseadas em clientes e volumes.

        Os resultados dos modelos estão disponível pelo filtro_CD no mapa como BSK - NEW_CD2 empregando o algoritmo DBSCAN. 

        Uma ferramenta de medida está incluida no gráfico para facilitar medidas entre dois pontos (estendendo-se para uma 'rota', de forma que vários pontos podem ser adicionados.)
        """)

    with st.spinner('Aguarde o processamento sobre os dados...'):
        fig1 = Figure(height=350, width=750)

        m = folium.Map(tiles="Stamen Terrain",
                       location=[-23.70984667472482, -46.85242934867622],
                       zoom_start=13,
                       prefer_canvas=True)
        fig1.add_child(m)

        f3 = folium.FeatureGroup("Casas De Ração")

        folium.Marker(
            location=[-23.71102102311727, -46.8557157004849],
            tooltip="Dino Rações",
        ).add_to(f3)

        f3.add_to(m)

        folium.LayerControl().add_to(m)

        minimap = MiniMap(toggle_display=True,
                          tile_layer='Stamen Terrain', width=100, height=100)
        minimap.add_to(m)

        m.add_child(MeasureControl())

        plugins.Fullscreen(
            position="topright",
            title="Expand me",
            title_cancel="Exit me",
            force_separate_button=True,
        ).add_to(m)

        folium_static(m)
