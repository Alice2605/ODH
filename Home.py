import streamlit as st
st.set_page_config(layout="wide", page_title="Home - Import Excel") # Configuration de la page

import pandas as pd
from functions import *
from donnees import *

st.title("Home - Importation du fichier Excel")

st.markdown('#### Choisissez le fichier Excel à importer')
st.markdown('##### :warning: **Attendez que ça finisse de charger** (barre bleue ci-dessous et "RUNNING" en haut à droite de la page) puis vous pourrez changer de page pour voir les diagrammes.')
st.write('\n')

uploaded_file = st.file_uploader("Ajoutez votre fichier Excel", type=['xls', 'xlsx']) # Espace pour ajouter le fichier excel qui sera traité

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.session_state.df = df
    st.success("Document chargé !")




