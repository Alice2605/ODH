import streamlit as st
import plotly.express as px
from functions import *
import pandas as pd


# Un seul centre
st.cache_data
def donnees_centre(df, id):
    df_centre = df[
        (df['ID_HOPITAL'] == id) &
        (df['IDPATIENT'].isin(df[df['PRODUIT1'].isin(['trastuzumab', 'trastuzumab emtansine', 'trastuzumab duocarmazine', 'trastuzumab deruxtecan'])]['IDPATIENT']))
    ]
    df_centre = df_centre[['IDPATIENT', 'SUB_NUM_PROTO', 'PROTO', 'STADE_TRT', 'DT1DATEADMP']]
    df_centre = df_centre.sort_values(by=['IDPATIENT', 'DT1DATEADMP'])

    df_trie_centre = df_trie(df_centre) # Crée la table avec les lignes de protocoles et leur fréquence

    return df_trie_centre


# TOUT
@st.cache_data
def donnees_tout(df):
    df_tout = df[
        (df['IDPATIENT'].isin(df[df['PRODUIT1'].isin(['trastuzumab', 'trastuzumab emtansine', 'trastuzumab duocarmazine', 'trastuzumab deruxtecan'])]['IDPATIENT']))
    ]
    df_tout = df_tout[['IDPATIENT', 'SUB_NUM_PROTO', 'PROTO', 'STADE_TRT', 'DT1DATEADMP']]
    df_tout = df_tout.sort_values(by=['IDPATIENT', 'DT1DATEADMP'])

    df_trie_tout = df_trie(df_tout)

    return df_trie_tout


# Sankey et sunburst
def fig(df_trie):
    colonnes = df_trie.columns[:-1].tolist()

    fig_sunburst = px.sunburst(df_trie, path=colonnes, values='VALUE')

    labels_reel, label_color, links = donnees_diagram(df_trie) # Récupère les variables de label, couleur, source, target et valeur
    fig_sankey = cree_sankey(labels_reel, label_color, links)

    return fig_sankey, fig_sunburst

