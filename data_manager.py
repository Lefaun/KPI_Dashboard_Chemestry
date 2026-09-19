import streamlit as st
import datetime

def init_state():
    """Initializes standard state variables in st.session_state."""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None

    if 'role' not in st.session_state:
        st.session_state.role = "Viewer"

    if 'cart' not in st.session_state:
        st.session_state.cart = []
        
    if 'tasks' not in st.session_state:
        # Mock Kanban tasks
        st.session_state.tasks = [
            {"id": 1, "title": "Setup Lab Equipment", "status": "Todo", "assignee": "Alice"},
            {"id": 2, "title": "Run Reaction A1", "status": "In Progress", "assignee": "Bob"},
            {"id": 3, "title": "Analyze Results B", "status": "In Progress", "assignee": "Alice"},
            {"id": 4, "title": "Prepare Presentation", "status": "Review", "assignee": "Charlie"},
            {"id": 5, "title": "Order Reagents", "status": "Done", "assignee": "David"}
        ]
        
    if 'events' not in st.session_state:
        # Mock Calendar Events
        today = datetime.date.today()
        st.session_state.events = [
            {"title": "Weekly R&D Sync", "date": today, "type": "Meeting"},
            {"title": "Equipment Calibration", "date": today + datetime.timedelta(days=2), "type": "Maintenance"}
        ]

def login(username, password):
    # Dummy authentication logic
    if username == "admin" and password == "admin":
        st.session_state.authenticated = True
        st.session_state.current_user = "Admin Paulo"
        st.session_state.role = "Admin"
        return True
    elif username == "user" and password == "user":
        st.session_state.authenticated = True
        st.session_state.current_user = "Researcher 1"
        st.session_state.role = "Researcher"
        return True
    return False

def logout():
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.session_state.role = "Viewer"
    st.session_state.cart = []
