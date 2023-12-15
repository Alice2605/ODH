import streamlit as st
# Nom de l'onglet dans le navigateur
st.set_page_config(layout="wide", page_title="Sunburst Diagram")


from functions import *
from donnees import *


st.markdown("# Sunburst diagram")


# Liste des options du menu déroulant
options = ['Sélectionner', 'CGFL', 'TOUT']

# Affichage du menu déroulant dans l'application Streamlit
selected_option = st.selectbox('Sélectionnez une option', options)


if selected_option == 'CGFL':

    fig_cgfl_sunburst.update_layout(#title_text="Patients ayant reçu du trastuzumab au CGFL", 
        #title_font_size=20,
        template="plotly_white",
                    
        margin={"t": 0, "r": 0, "b": 0, "l": 0},
        width=1800,  # Largeur du graphique
        height=1100  # Hauteur du graphique
        ) # Change la taille de police du TITRE
    
    fig_cgfl_sunburst.update_traces(textfont_size=20) # Change la taille de police du texte des NOEUDS
    st.plotly_chart(fig_cgfl_sunburst)



if selected_option == 'TOUT':

    fig_tout_sunburst.update_layout(#title_text="Patients ayant reçu du trastuzumab (tous centres)", 
        #title_font_size=20,
        template="plotly_white",
                    
        margin={"t": 0, "r": 0, "b": 0, "l": 0},
        width=1800,  # Largeur du graphique
        height=1100  # Hauteur du graphique
        ) # Change la taille de police du TITRE
    
    fig_tout_sunburst.update_traces(textfont_size=20) # Change la taille de police du texte des NOEUDS
    st.plotly_chart(fig_tout_sunburst)
