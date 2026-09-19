import streamlit as st

def show():
    st.title("📋 Kanban Board")
    st.markdown("Manage team tasks and assignments.")
    
    # Kanban layout
    cols = st.columns(4)
    statuses = ["Todo", "In Progress", "Review", "Done"]
    
    for idx, status in enumerate(statuses):
        with cols[idx]:
            st.markdown(f"<div class='kanban-column'><h3>{status}</h3>", unsafe_allow_html=True)
            for task in st.session_state.tasks:
                if task["status"] == status:
                    badge_class = "badge-white"
                    if status == "In Progress": badge_class = "badge-cyan"
                    elif status == "Review": badge_class = "badge-orange"
                    elif status == "Done": badge_class = "badge-green"
                    
                    st.markdown(f"""
                    <div class='task-card'>
                        <h4>{task['title']}</h4>
                        <p>👤 {task['assignee']}</p>
                        <span class='{badge_class}'>{status}</span>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
    st.divider()
    with st.expander("Add New Task"):
        with st.form("new_task"):
            title = st.text_input("Task Title")
            assignee = st.text_input("Assignee")
            submit = st.form_submit_button("Add Task")
            if submit and title:
                st.session_state.tasks.append({
                    "id": len(st.session_state.tasks) + 1,
                    "title": title,
                    "status": "Todo",
                    "assignee": assignee
                })
                st.rerun()
