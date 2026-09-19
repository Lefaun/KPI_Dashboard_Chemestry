import streamlit as st
import time

def show():
    st.title("✉️ Notifications & Comms")
    st.markdown("Dispatch emails and WhatsApp messages to the team.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Send Email")
        with st.form("email_form"):
            recipient = st.text_input("To:")
            subject = st.text_input("Subject:")
            body = st.text_area("Message:")
            if st.form_submit_button("Send Email"):
                with st.spinner("Sending email..."):
                    time.sleep(1)
                st.success("Email dispatched via SMTP!")
                
    with col2:
        st.subheader("Send WhatsApp")
        with st.form("wa_form"):
            phone = st.text_input("Phone Number:")
            msg = st.text_area("Message:")
            if st.form_submit_button("Send WhatsApp"):
                with st.spinner("Connecting to Twilio..."):
                    time.sleep(1)
                st.success("WhatsApp message dispatched!")
