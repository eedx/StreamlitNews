import streamlit as st


## --- COLUMNS DEFINITION
st.title('Uso de herramientas', anchor=False)
st.write('\n')

## --- COLUMNS DEFINITION
col1, col2 = st.columns(2, gap='large', vertical_alignment='top')

with st.container():
    with col1:
        st.header('Chatbot Educativo')
        with st.expander('Ver más'):
            st.markdown(
                '''
                En la barra inferior puedes realizar consultas referentes a diversos temas para combatir la desinformación y noticias engañosas, verificar información sobre Colombia o mejorar tus conocimientos con el asistente entrenado para responder consultas rápidamente. Por sesión es posible realizar hasta `10` consultas.
                '''
            )

    with col2:
        st.header('Analizador de Noticias', anchor=False)
        with st.expander('Ver más'):
            st.markdown(
                '''
                En esta sección podrás pegar el contenido de algún artículo de noticias, y al enviarlo será analizado, indicando tres parámetros fundamentales con sus explicaciones correspondientes:
                * Probabilidad de desinformación
                * Análisis de sentimientos
                * Probabilidad de discurso de odio
                '''
            )
            

st.write('\n')
st.write('\n')
st.markdown('***')
st.markdown('En caso de presentar alguna duda, puedes contactarme en la sección :blue-background[Sobre Mí]')