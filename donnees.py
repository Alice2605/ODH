import streamlit as st
import plotly.express as px
from functions import *
import pandas as pd

"""
excel_file_path = 'Export_base_ODH_SEIN.xlsx'
df = pd.read_excel(excel_file_path)
"""

#from Sankey_diagram_from_excel import uploaded_file

#df = pd.read_excel(uploaded_file)

#################### CGFL
st.cache_data
def donnees_cgfl(df):
    df_cgfl = df[
        (df['ID_HOPITAL'] == 210987731) &
        (df['IDPATIENT'].isin(df[df['PRODUIT1'].isin(['trastuzumab', 'trastuzumab emtansine', 'trastuzumab duocarmazine', 'trastuzumab deruxtecan'])]['IDPATIENT']))
    ]
    df_cgfl = df_cgfl[['IDPATIENT', 'SUB_NUM_PROTO', 'PROTO', 'STADE_TRT', 'DT1DATEADMP']]
    df_cgfl = df_cgfl.sort_values(by=['IDPATIENT', 'DT1DATEADMP'])


    df_trastuzumab_cgfl = df_to_df_trastuzumab(df_cgfl) # Crée la table avec les lignes de protocoles et leur fréquence

    colonnes = df_trastuzumab_cgfl.columns[:-1].tolist()


    fig_cgfl_sunburst = px.sunburst(df_trastuzumab_cgfl[df_trastuzumab_cgfl != "NaN"], path=colonnes, values='VALUE') # Sunburst

    df_trastuzumab_cgfl.fillna("NaN", inplace=True)

    labels_reel, label_color, links = donnees_diagram(df_trastuzumab_cgfl) # Récupère les variables de label, couleur, source, target et valeur
    fig_cgfl_sankey = cree_sankey(labels_reel, label_color, links) # Sankey

    return fig_cgfl_sankey



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

    fig_tout_sunburst = px.sunburst(df_trastuzumab_tout[df_trastuzumab_tout != "NaN"], path=colonnes, values='VALUE')

    labels_reel, label_color, links = donnees_diagram(df_trastuzumab_tout) # Récupère les variables de label, couleur, source, target et valeur
    fig_tout_sankey = cree_sankey(labels_reel, label_color, links)

    return fig_tout_sankey




