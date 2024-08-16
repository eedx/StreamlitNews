import streamlit as st
import requests
import time
import re

webhook = st.secrets['WEBHOOK_URL']


## --- EMAIL VALIDATION
def is_valid_email(email) -> bool:
    """
    Checks whether the email account entered by user is correct

    Args:
        email (str): Email account to verify

    Returns:
        bool: Pattern verification boolean
    """   
     
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None


## --- INPUT VERIFICATION
def input_verification(name, email, message) -> None:
    """
    Verifies if the input data is complete

    Args:
        name (str): Sender's name
        email (str): Sender's email address
        message (str): Message
    """    
    if not webhook:
        st.error('El servicio de email no ha sido establecido. Intente nuevamente más tarde')
        st.stop()
    if not name:
        st.error('Por favor ingresa tu nombre')
        st.stop()
    if not email:
        st.error('Por favor ingresa tu correo electrónico')
        st.stop()
    if not message:
        st.error('Por favor ingresa un mensaje')
        st.stop()


## --- EMAIL SENDING FORM
def contact_form() -> None:
    """
    Creates the Contact me form and sends the message
    """    
    
    with st.form('contact_form'):
        name = st.text_input('Nombre')
        email = st.text_input('Correo')
        message = st.text_area('Mensaje')
        
        submit_btn = st.form_submit_button('Enviar')
        
        if email and not is_valid_email(email):
            st.write('Por favor introduce un correo electrónico válido')
        else:
            if submit_btn:
                input_verification(name, email, message)
                
                data = {
                    'email': email,
                    'name': name,
                    'message': message
                }
                response = requests.post(webhook, json=data)
                
                if response.status_code == 200:
                    time.sleep(0.04)
                    st.success('¡Mensaje enviado exitosamente! 🚀')
                else:
                    st.error('Ocurrió un error al enviar tu mensaje. Intenta nuevamente')