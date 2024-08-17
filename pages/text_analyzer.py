import streamlit as st
import openai
import json


st.title('Análisis de Noticias')


## --- SESION STATE INITIALIZATION
if 'messages' not in st.session_state:
    st.session_state.messages = []


## --- OPENAI KEY CONFIGURATION
openai.api_key = st.secrets['OPENAI_API_KEY']


## --- CHATBOT INTERACTIONS FUNCTION
def get_chatbot_response(prompt: str) -> dict:
    """
    Chatbot config function, delivers a generator with the answer

    Args:
        prompt (str): User input

    Returns:
        dict: JSON object with text classification from OpenAI API
    """    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You're an advanced text classifier with a vast knowledge in news, misinformation and Colombian politics (both natinally and internationally). Your job is to classify text within 3 parameters: misinformation_prob (that indicates the probability of a new being misinformation), sentiment_score (from 1 to 3, being 3 positive, 1 negative and 2 neutral), and hate_speech_prob (containing the probability of an article to contain hate speech). The answer should be a json object, containing the misinformation_prob, sentiment_score, hate_speech_prob and explanations, containing their corresponding short explanations in spanish"},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.17,
        presence_penalty=0,
        response_format={
            "type": "json_object"
        }
    )
    message = response.choices[0].message.content

    return json.loads(message)


## --- RESPONSE VISUALIZATION
def get_delta(response: dict) -> dict:
    """
    Get emojis for a simple and visual representation on results

    Args:
        response (dict): AI assistant's output dictionary  

    Returns:
        dict: Object with corresponding delta values represented as emojis
    """    
    delta = {}
    for key in response.keys():
        if 'explanation' in key:
            continue
        
        if isinstance(response[key], int):
            value = 1 / response[key]
        else:
            value = response[key]
            
        if value < 0.5:
            delta[key] = '-😁'
        elif value > 0.5:
            delta[key] = '😟'
        else:
            delta[key] = '😐'
    
    return delta


## --- TOOLS COLUMNS
col1, col2, col3 = st.columns(
    3, 
    gap='medium', 
    vertical_alignment='top'
)


## --- CONTAINER LOGIC
def analyzer_logic():
    """
    This function runs the text input and activates the analysis tool
    """    
    with st.container(border=True):
        text = st.chat_input('Introduce el contenido de una noticia para analizar')
        if text:
            st.write(text)    

            response = get_chatbot_response(text)
            delta_dict  = get_delta(response)
            
            with st.empty():
                with col1:
                    st.metric(
                        label='Desinformación',
                        value=f'{response["misinformation_prob"] * 100}%',
                        delta=delta_dict['misinformation_prob'],
                        delta_color='inverse'
                    )
                    with st.expander('Ver explicación'):
                        st.write(response['explanations']['misinformation_prob'])
                        
                with col2:
                    st.metric(
                        label='Sentimiento',
                        value=f'{response["sentiment_score"]}',
                        delta=delta_dict['sentiment_score'],
                        delta_color='inverse'
                    )
                    with st.expander('Ver explicación'):
                        st.write(response['explanations']['sentiment_score'])
                        
                with col3:
                    st.metric(
                        label='Discurso de odio',
                        value=f'{response["hate_speech_prob"] * 100}%',
                        delta=delta_dict['hate_speech_prob'],
                        delta_color='inverse'
                    )
                    with st.expander('Ver explicación'):
                        st.write(response['explanations']['hate_speech_prob'])
                
                
analyzer_logic()