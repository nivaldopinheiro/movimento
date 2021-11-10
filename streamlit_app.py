import streamlit as st
from streamlit_folium import folium_static
import folium
from branca.element import Figure
import pandas as pd
import joblib
import folium.plugins as plugins
from folium.plugins import HeatMap
import numpy as np
from folium.plugins import MiniMap
from folium.plugins import MeasureControl
from PIL import Image
import plotly.express as px
import streamlit.components.v1 as components
import requests


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


icon = Image.open("static\icone.jpg")

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
        st.image(Image.open("static/logo.jpeg"), width=200)

    st.write(
        """

        """)

    st.markdown('### Animais de Rua de Itapecerica da Serra')
    
    st.write(
        """

        """)

    st.write(
        """
        Somos um movimento que luta por políticas públicas para os animais de rua.

        Apresentamos e divulgamos os principais problemas e dificuldades da causa animal e lutamos para manter ativos nossos projetos como:

        - Alimente um Cão de Rua
        - Projeto Farmacinha Popular
        - Roupinhas Para Animais de Rua
        
        """)

    st.write(
        """

        """)

    #https://www.facebook.com/777922895900095/videos/431890404709544

    mid_video1, t1_video, mid_video = st.columns([5, 10, 5])
    with t1_video:
        video1 = open("static/video.mp4", "rb") 
        st.video(video1)

        st.write("""
        Video credit:
        Creator: João.
        License: Free for personal use.
        """)

    t1_foto, t2_foto = st.columns([10, 10])
    with t1_foto:
        st.image(Image.open("static/foto8.jpeg"))

    with t2_foto:
        # use_column_width=True)
        st.image(Image.open("static/foto5.jpeg"))

    t3_foto, t4_foto = st.columns([10, 10])
    with t3_foto:
        st.image(Image.open("static/foto7.jpeg"))

    with t4_foto:
        # use_column_width=True)
        st.image(Image.open("static/foto16.jpeg"))

    st.sidebar.write("---")

    st.markdown('### Parcerias')

    st.write(
        """
        O crime de abandono de animais é constante e tem se tornado algo maior, o grupo antes mesmo do Projeto Integrador já conhecia a ONG Animais de Rua Itapecerica da Serra e sempre apoiou o Movimento, estando desde sempre nesta luta para sanar a fome e sede animal, porém a falta de recurso e reconhecimento, são os principais motivos que os impossibilita de realmente traçar o objetivo final, vendo isso, para ajudar o Movimento de alguma forma decidimos criar um portal onde estará disponível adoção de animais, parceria entre casas de ração e também a divulgação do seu trabalho.
        
        Esse site foi desenvolvido como parte de Projeto Integrador da Universidade Virtual do Estado de São Paulo (UNIVESP), Polo de Itapecerica da Serra, com os integrantes Adriano, Cláudio, Jéssica, João, Kelvin e Nivaldo.""")

elif study == 'Informações de Animais':
    # functions end here, title, sidebar setting and descriptions start here
    t1, mid, t2 = st.columns([20, 1, 10])
    with t1:
        st.markdown('# Movimento Mãos por Patas')

    with t2:
        # use_column_width=True)
        st.image(Image.open("static/logo.jpeg"), width=200)

    st.write(
        """
        O objetivo desse site é permitir uma maior visibilidade sobre o trabalho desenvolvido na cidade de Itapecerica da Serra.
        """)

    t1_A, t2_B, t3_C = st.columns([10, 10, 10])
    with t1_A:
        st.image(Image.open("static/foto1.jpeg"))

    with t2_B:
        st.image(Image.open("static/foto2.jpeg"))
    
    with t3_C:
        st.image(Image.open("static/foto3.jpeg"))

    t4_A, t5_B, t6_C = st.columns([10, 10, 10])
    with t4_A:
        st.image(Image.open("static/foto4.jpeg"))

    with t5_B:
        st.image(Image.open("static/foto6.jpeg"))
    
    with t6_C:
        st.image(Image.open("static/foto9.jpeg"))

    t7_A, t8_B, t9_C = st.columns([10, 10, 10])
    with t7_A:
        st.image(Image.open("static/foto10.jpeg"))

    with t8_B:
        st.image(Image.open("static/foto11.jpeg"))
    
    with t9_C:
        st.image(Image.open("static/foto12.jpeg"))

    with st.expander("Expanda para cadastro de animais"):
        st.markdown('### Cadastro Inicial ')

elif study == 'Informações de Casas de Ração':

    t1, mid, t2 = st.columns([20, 1, 10])
    with t1:
        st.markdown('# Movimento Mãos por Patas')

    with t2:
        # use_column_width=True)
        st.image(Image.open("static/logo.jpeg"), width=200)

    st.write(
        """
        Para entender e verificar o posicionamento atual das casas de ração um mapa foi desenvolvido.
        
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
