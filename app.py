import streamlit as st
import data_manager as dm

# Initialize session state
dm.init_state()

# Page config
st.set_page_config(page_title="BioChem Dashboard", page_icon="🧪", layout="wide")

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("styles.css")

# Import pages
from pages_module import auth, shop, workflow, kanban, spc_control, calendar_view, notifications

# Sidebar Navigation
with st.sidebar:
    st.title("🧪 BioChem R&D")
    
    if st.session_state.authenticated:
        st.markdown(f"**User**: {st.session_state.current_user}")
        st.markdown(f"**Role**: {st.session_state.role}")
        
        pages = {
            "Workflow Models": workflow,
            "Kanban Board": kanban,
            "SPC Control": spc_control,
            "Calendar": calendar_view,
            "Notifications": notifications,
            "Services Shop": shop,
            "Account": auth
        }
        
        selection = st.radio("Navigation", list(pages.keys()))
        
        st.divider()
        st.info("System Status: Online")
    else:
        pages = {"Login": auth}
        selection = "Login"

# Route to selected page
pages[selection].show()
