import streamlit as st

from forms.contact import contact_form


## --- CONTACT ME FORM FUNCTION
@st.dialog('Contáctame')
def show_form():
    contact_form()


## --- COLUMNS DEFINITION
col1, col2 = st.columns(2, gap='medium', vertical_alignment='center')

with col1:
    st.image('./assets/picture.png', width=260)

with col2:
    st.title('Eduardo Peña', anchor=False)
    
    st.markdown(
        ':violet-background[ML Engineer | Data Analyst]'
    )
    st.write(
        'Ofrezco soluciones impulsadas por IA y genero desarrollos enfocados en mejoras basadas en datos\n'
    )

    if st.button('Contáctame ✉️'):
        show_form()


## --- EXPERIENCE 
st.write('\n')
st.write('\n')
st.subheader(':blue-background[Experiencia y Cualificaciones]', anchor=False)
st.write(
    '''
    - 4 años en análisis de datos y riesgos
    - Conocimientos avanzados en Python
    - 1 año en desarrollo de proyectos impulsados por Machine Learning y Deep Learning (Computer Vision, NLP y Clasificación de Clientes)
    - Proficiencia en estadística y diversas ramas científicas
    - Capacidades de liderazgo y trabajo en equipo, con alto sentido de iniciativa
    '''
)


## --- SKILLS
st.write('\n')
st.subheader(':blue-background[Habilidades]', anchor=False)
st.write(
    '''
    - Programación: Python (Tensorflow, Scikit-learn, TFX, Pandas), SQL
    - Visualización de Datos: Tableau, PowerBI, MS Excel, Matplotlib
    - Modelado ML: Random Forest, DNN, Clustering (KNN), Regressions 
    - Bases de datos: MySQL
    - Desarrollo web: HTML, CSS, JavaScript, ReactJS, Bootstrap
    - Programación en la nube: Azure Web Services
    '''
)

