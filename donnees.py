import streamlit as st
import plotly.express as px
from functions import *
import pandas as pd


#################### Un seul centre
st.cache_data
def donnees_centre(df, id):
    df_centre = df[
        (df['ID_HOPITAL'] == id) &
        (df['IDPATIENT'].isin(df[df['PRODUIT1'].isin(['trastuzumab', 'trastuzumab emtansine', 'trastuzumab duocarmazine', 'trastuzumab deruxtecan'])]['IDPATIENT']))
    ]
    df_centre = df_centre[['IDPATIENT', 'SUB_NUM_PROTO', 'PROTO', 'STADE_TRT', 'DT1DATEADMP']]
    df_centre = df_centre.sort_values(by=['IDPATIENT', 'DT1DATEADMP'])


    df_trastuzumab_centre = df_to_df_trastuzumab(df_centre) # Crée la table avec les lignes de protocoles et leur fréquence

    colonnes = df_trastuzumab_centre.columns[:-1].tolist()

    
    #fig_centre_sunburst = px.sunburst(df_trastuzumab_centre[df_trastuzumab_centre != "NaN"], path=colonnes, values='VALUE') # Sunburst
    fig_centre_sunburst = px.sunburst(df_trastuzumab_centre, path=colonnes, values='VALUE') # Sunburst
    

    labels_reel, label_color, links = donnees_diagram(df_trastuzumab_centre) # Récupère les variables de label, couleur, source, target et valeur
    fig_centre_sankey = cree_sankey(labels_reel, label_color, links) # Sankey

    return fig_centre_sankey, fig_centre_sunburst



#################### TOUT
@st.cache_data
def donnees_tout(df):
    df_tout = df[
        (df['IDPATIENT'].isin(df[df['PRODUIT1'].isin(['trastuzumab', 'trastuzumab emtansine', 'trastuzumab duocarmazine', 'trastuzumab deruxtecan'])]['IDPATIENT']))
    ]
    df_tout = df_tout[['IDPATIENT', 'SUB_NUM_PROTO', 'PROTO', 'STADE_TRT', 'DT1DATEADMP']]
    df_tout = df_tout.sort_values(by=['IDPATIENT', 'DT1DATEADMP'])


    df_trastuzumab_tout = df_to_df_trastuzumab(df_tout)

    colonnes = df_trastuzumab_tout.columns[:-1].tolist()

    fig_tout_sunburst = px.sunburst(df_trastuzumab_tout, path=colonnes, values='VALUE')

    labels_reel, label_color, links = donnees_diagram(df_trastuzumab_tout) # Récupère les variables de label, couleur, source, target et valeur
    fig_tout_sankey = cree_sankey(labels_reel, label_color, links)

    return fig_tout_sankey, fig_tout_sunburst




