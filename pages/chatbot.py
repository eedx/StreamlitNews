import streamlit as st
import openai
import time


## --- OPENAI KEY CONFIGURATION
openai.api_key = st.secrets['OPENAI_API_KEY']


## --- DEFINING QUERY LIMITS
MAX_QUERIES = 10
st.title("Chatbot Educativo")
st.write(f"Puedes realizar hasta {MAX_QUERIES} consultas en esta sesión.")


## --- SESION STATE INITIALIZATION
if 'query_count' not in st.session_state:
    st.session_state['query_count'] = 0
if 'messages' not in st.session_state:
    st.session_state.messages = []


## --- CHATBOT INTERACTIONS FUNCTION
def get_chatbot_response(prompt: str):
    """
    Chatbot config function, delivers a generator with the answer

    Args:
        prompt (str): User input

    Returns:
        str: Answer message from OpenAI API
    """    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You're an expert educative assistant with a vast knowledge in news, misinformation and Colombian politics. Your job is to answer questions in order to help people learn about those topics. The answer should be in Spanish and trying to be as concise as possible"},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.17,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )
    message = response.choices[0].message.content

    #for word in message.split():
    #    yield word + ' '
    #    time.sleep(0.02)

    # NOTA: BUSCAR CÓMO USAR UN GENERADOR SIN MODIFICAR EL FORMATO DEL TEXTO
    # PARA DAR EL EFECTO DE ANIMACIÓN AL REALIZAR CONSULTAS

    return message


## --- MESSAGE WRITING
def message_main():
    """
    Main function to create the markdown for the conversation with the chatbot
    """    
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    if st.session_state['query_count'] < MAX_QUERIES:
        if prompt := st.chat_input('Escribe aquí tu mensaje:'):
            st.session_state.messages.append({
                'role': 'user',
                'content': prompt
            })

            with st.chat_message('user'):
                st.markdown(prompt)

            with st.chat_message('assistant'):
                response = st.write(get_chatbot_response(prompt=prompt))
            st.session_state.messages.append({
                'role': 'assistant',
                'content': response
            })
            st.session_state['query_count'] += 1
            st.markdown(f"Consultas restantes: :blue-background[{MAX_QUERIES - st.session_state['query_count']}]")

    else:
        st.write("Has alcanzado el límite de consultas permitidas.")


message_main()