import streamlit as st
import datetime

def show():
    st.title("📅 Calendar & Events")
    st.markdown("Upcoming meetings and lab maintenance.")
    
    for event in st.session_state.events:
        badge = "badge-cyan" if event["type"] == "Meeting" else "badge-orange"
        st.markdown(f"""
        <div class='dashboard-card' style='display:flex; justify-content:space-between; align-items:center;'>
            <div>
                <h4>{event['title']}</h4>
                <p style='color:var(--text-muted); margin:0;'>{event['date'].strftime('%B %d, %Y')}</p>
            </div>
            <span class='{badge}'>{event['type']}</span>
        </div>
        """, unsafe_allow_html=True)
        
    with st.expander("Schedule New Event"):
        with st.form("new_event"):
            title = st.text_input("Event Title")
            date = st.date_input("Date")
            type = st.selectbox("Type", ["Meeting", "Maintenance", "Deadline"])
            submit = st.form_submit_button("Schedule")
            if submit and title:
                st.session_state.events.append({
                    "title": title,
                    "date": date,
                    "type": type
                })
                st.rerun()
