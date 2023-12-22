import streamlit as st
# Nom de l'onglet dans le navigateur
st.set_page_config(layout="wide", page_title="Données")


from functions import *
from donnees import *

df = st.session_state.df

# Liste des centres
liste_hopitaux = sorted(df["ID_HOPITAL"].unique().tolist())

st.markdown("# Données triées par séquence de protocoles")



# Liste des options du menu déroulant
options = ['Sélectionner', 'TOUT'] + liste_hopitaux

# Affichage du menu déroulant dans l'application Streamlit
selected_option = st.selectbox('Sélectionnez un centre', options)


if selected_option in liste_hopitaux:
    df_trie_centre = donnees_centre(df, selected_option)
    st.dataframe(df_trie_centre)

if selected_option == 'TOUT':
    df_trie_tout = donnees_tout(df)
    st.dataframe(df_trie_tout)

