import streamlit as st
import smtplib
import time


def contact_form() -> None:
    """
    Creates the Contact me form and sends the message
    """    
    with st.form('contact_form'):
        name = st.text_input('Nombre')
        email = st.text_input('Correo')
        message = st.text_area('Mensaje')
        submit_btn = st.form_submit_button('Enviar')

        if submit_btn:
            with smtplib.SMTP('localhost') as smtp:
                smtp.starttls()
                smtp.sendmail(from_addr=email, to_addrs=st.secrets['SMTP_USER'], msg=message)

            time.sleep(0.05)

            st.success('¡Mensaje enviado exitosamente!')


def msg_sending(message: str) -> None:
    """
    Sends the email when clicking the submit button
    """    

    with smtplib.SMTP('localhost') as smtp:
        smtp.send_message(message)
