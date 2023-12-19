import streamlit as st
st.set_page_config(layout="wide", page_title="Home - Import Excel") # Configuration de la page

import pandas as pd
from functions import *
from donnees import *







st.markdown("# Home")




uploaded_file = st.file_uploader("Ajoutez votre fichier Excel") # Espace pour ajouter le fichier excel qui sera traité

if uploaded_file is not None: # Une fois qu'un fichier est importé

    df = pd.read_excel(uploaded_file) # DataFrame à partir du fichier

    # Liste des options du menu déroulant
    options = ['Sélectionner', 'CGFL', 'TOUT']

    # Affichage du menu déroulant dans l'application Streamlit
    selected_option = st.selectbox('Sélectionnez une option', options)










