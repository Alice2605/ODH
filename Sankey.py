import streamlit as st
st.set_page_config(layout="wide", page_title="Sankey Diagram") # Configuration de la page

import pandas as pd
from functions import *
from donnees import *



st.markdown(f"<h1 style='text-align: center;'>Diagrammes de Sankey ODH, médicaments injectables par protocole</h1>", unsafe_allow_html=True) # Titre

uploaded_file = st.file_uploader("Ajoutez votre fichier Excel") # Espace pour ajouter le fichier excel qui sera traité

if uploaded_file is not None: # Une fois qu'un fichier est importé

    df = pd.read_excel(uploaded_file) # DataFrame à partir du fichier


    # Liste des options du menu déroulant
    options = ['Sélectionner', 'CGFL', 'TOUT']

    # Affichage du menu déroulant dans l'application Streamlit
    selected_option = st.selectbox('Sélectionnez une option', options)


    # Si CGFL sélectionné dans le menu déroulant
    if selected_option == 'CGFL':
        fig_cgfl_sankey, _ = donnees_cgfl(df) # , _ for sunburst

        fig_cgfl_sankey.update_layout(title_text="Patients ayant reçu du trastuzumab au CGFL", 
                        title_font_size=30,
                        width=1700  # Largeur du graphique
                        ) # Change la taille de police du TITRE
        fig_cgfl_sankey.update_traces(textfont_size=12) # Change la taille de police du texte des NOEUDS
        st.plotly_chart(fig_cgfl_sankey) # Affiche le graphique


    # Si TOUT sélectionné dans le menu déroulant (tous les centres)
    if selected_option == 'TOUT':
        fig_tout_sankey, _ = donnees_tout(df)

        fig_tout_sankey.update_layout(title_text="Tous les patients ayant reçu du trastuzumab", 
                        title_font_size=30, 
                        width=1700  # Largeur du graphique
                        ) # Change la taille de police du TITRE
        fig_tout_sankey.update_traces(textfont_size=12) # Change la taille de police du texte des NOEUDS
        st.plotly_chart(fig_tout_sankey) # Affiche le graphique





