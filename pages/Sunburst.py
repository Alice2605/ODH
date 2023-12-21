import streamlit as st
# Nom de l'onglet dans le navigateur
st.set_page_config(layout="wide", page_title="Sunburst Diagram")


from functions import *
from donnees import *

df = st.session_state.df

# Liste des centres
liste_hopitaux = sorted(df["ID_HOPITAL"].unique().tolist())

st.markdown("# Sunburst diagram")



# Liste des options du menu déroulant
options = ['Sélectionner', 'TOUT'] + liste_hopitaux

# Affichage du menu déroulant dans l'application Streamlit
selected_option = st.selectbox('Sélectionnez un centre', options)


if selected_option in liste_hopitaux:
    _, fig_centre_sunburst = donnees_centre(df, selected_option)
    fig_centre_sunburst.update_layout(
        #title_text="Patients ayant reçu du trastuzumab au centre", 
        #title_font_size=20,
        template="plotly_white",
        
        margin={"t": 0, "r": 0, "b": 0, "l": 0},
        width=1800,  # Largeur du graphique
        height=1100  # Hauteur du graphique
        ) # Change la taille de police du TITRE
    
    fig_centre_sunburst.update_traces(textfont_size=20) # Change la taille de police du texte des NOEUDS
    st.plotly_chart(fig_centre_sunburst)

    st.download_button(label="Télécharger le graph au format html", data=fig_centre_sunburst.to_html(full_html=False), file_name="Sunburst_diagram.html")



if selected_option == 'TOUT':
    _, fig_tout_sunburst = donnees_tout(df)
    fig_tout_sunburst.update_layout(
        #title_text="Patients ayant reçu du trastuzumab (tous centres)", 
        #title_font_size=20,
        template="plotly_white",
        
        margin={"t": 0, "r": 0, "b": 0, "l": 0},
        width=1800,  # Largeur du graphique
        height=1100  # Hauteur du graphique
        ) # Change la taille de police du TITRE
    
    fig_tout_sunburst.update_traces(textfont_size=20) # Change la taille de police du texte des NOEUDS
    st.plotly_chart(fig_tout_sunburst)
    st.download_button(label="Télécharger le graph au format html", data=fig_tout_sunburst.to_html(full_html=False), file_name="Sunburst_diagram_tout.html")

