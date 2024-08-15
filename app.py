import streamlit as st


## --- MAIN CONFIG
st.set_page_config(page_title="Analizador de Noticias", page_icon="📖")


## --- PAGE SETUP
about_page = st.Page(
    page='pages/about_me.py',
    title='Sobre Mí',
    icon=':material/account_circle:',
    default=True
)

chatbot_page = st.Page(
    page='pages/chatbot.py',
    title='Chatbot Educativo',
    icon=':material/robot_2:'
)

analyzer_page = st.Page(
    page='pages/text_analyzer.py',
    title='Analizador de Texto',
    icon=':material/analytics:'
)


## --- NAVIGATION
pg = st.navigation(
        {
            "Info": [about_page],
            "Herramientas": [chatbot_page, analyzer_page],
        }
    )


## --- COMMON 
st.sidebar.text('Made with 🤍 by eedx')
st.logo('./assets/logo.png')

## --- RUN NAVIGATION
pg.run()