import streamlit as st
import data_manager as dm

def show():
    st.title("🔐 Authentication")
    
    if st.session_state.authenticated:
        st.success(f"Logged in as {st.session_state.current_user} ({st.session_state.role})")
        if st.button("Logout", key="logout_btn"):
            dm.logout()
            st.rerun()
    else:
        st.markdown("Please log in to access the R&D Dashboard.")
        with st.form("login_form"):
            user = st.text_input("Username")
            pwd = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                if dm.login(user, pwd):
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid credentials. Try admin/admin or user/user")
