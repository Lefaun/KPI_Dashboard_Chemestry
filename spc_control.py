import streamlit as st
import chemistry_models as cm

def show():
    st.title("📈 SPC Control Zones")
    st.markdown("Statistical Process Control for Batch Yields.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        fig = cm.generate_spc_chart()
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader("Control Summary")
        st.markdown("""
        * **Target Yield**: 100%
        * **Process Mean**: ~100%
        * **Standard Dev**: 5%
        * **Out of Control Points**: 0
        """)
        
        st.info("Process is stable and in control.")
