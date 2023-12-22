import streamlit as st
st.set_page_config(layout="wide", page_title="Sankey Diagram") # Configuration de la page

import pandas as pd
from functions import *
from donnees import *


df = st.session_state.df

# Liste des centres
liste_hopitaux = sorted(df["ID_HOPITAL"].unique().tolist())

st.title("Diagrammes de Sankey") # Titre


# Liste des options du menu déroulant
options = ['Sélectionner', 'TOUT'] + liste_hopitaux

# Affichage du menu déroulant dans l'application Streamlit
selected_option = st.selectbox('Sélectionnez un centre', options)


# Si un centre est sélectionné dans le menu déroulant
if selected_option in liste_hopitaux:
    df_trie_centre = donnees_centre(df, selected_option)
    fig_centre_sankey, _ = fig_tout(df_trie_centre) 

    fig_centre_sankey.update_layout(
        #title_text="Patients ayant reçu du trastuzumab au centre", 
        #title_font_size=30,
        width=1600  # Largeur du graphique
        ) # Change la taille de police du TITRE
    fig_centre_sankey.update_traces(textfont_size=12) # Change la taille de police du texte des NOEUDS
    st.plotly_chart(fig_centre_sankey) # Affiche le graphique

    st.download_button(label="Télécharger le diagramme au format html", data=fig_centre_sankey.to_html(full_html=False), file_name="Sankey_diagram.html")


# Si TOUT sélectionné dans le menu déroulant (tous les centres)
if selected_option == 'TOUT':
    df_trie_tout = donnees_tout(df)
    fig_tout_sankey, _ = fig_tout(df_trie_tout)

    fig_tout_sankey.update_layout(
        title_text="Tous les patients ayant reçu du trastuzumab", 
        title_font_size=30, 
        width=1600  # Largeur du graphique
        ) # Change la taille de police du TITRE
    fig_tout_sankey.update_traces(textfont_size=12) # Change la taille de police du texte des NOEUDS
    st.plotly_chart(fig_tout_sankey) # Affiche le graphique

    st.download_button(label="Télécharger le diagramme au format html", data=fig_tout_sankey.to_html(full_html=False), file_name="Sankey_diagram_tout.html")

