import streamlit as st


## --- MAIN CONFIG
st.set_page_config(
    page_title="Analizador de Noticias", 
    page_icon="📖",
    layout='wide')


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
    title='Análisis de Noticias',
    icon=':material/analytics:'
)

about_tool_page = st.Page(
    page='pages/about_tool.py',
    title='Este sitio',
    icon=':material/info:'
)

how_to_page = st.Page(
    page='pages/how_to.py',
    title='Esta herramienta',
    icon=':material/handyman:'
)


## --- NAVIGATION
pg = st.navigation(
        {
            "Info": [about_page],
            "Herramientas": [chatbot_page, analyzer_page],
            "Acerca de": [about_tool_page, how_to_page]
        }
    )


## --- COMMON 
with st.sidebar:
    st.text('Made with 🤍 by eedx')
    st.html('''
            <br>
            <div style="width:100%;text-align:center;">
                <a href="https://github.com/eedx/StreamlitNews" style="float:center">
                    <img src="./app/static/github-logo.png" alt="GitHub" title="Personal GitHub" width="50px"></img>
                </a>
            </div>
    ''')
st.logo('./assets/logo.png')


## --- RUN NAVIGATION
pg.run()