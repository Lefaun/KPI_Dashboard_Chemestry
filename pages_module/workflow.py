import streamlit as st
import chemistry_models as cm

def show():
    st.title("🧪 Chemistry Workflow Dashboard")
    st.markdown("Run predictive R&D simulations.")
    
    st.markdown(f"""
    <div style='display:flex; justify-content:space-between;'>
        <div class='dashboard-card' style='flex:1; margin-right:10px;'>
            <small style='color: #fbfba8;'>⚙️ Lotes em Produção</small>
            <h2 style='color: white; margin: 5px 0 0 0;'>24</h2>
            <span style='color: #fbfba8; font-size: 0.8rem;'>12 finalizados</span>
        </div>
        <div class='dashboard-card' style='flex:1; margin-right:10px;'>
            <small style='color: #fbfba8;'>💰 Receita R&D Gerada</small>
            <h2 style='color: white; margin: 5px 0 0 0;'>45,000.00 €</h2>
            <span style='color: #00f2fe; font-size: 0.8rem;'>Vendas & Serviços</span>
        </div>
        <div class='dashboard-card' style='flex:1; margin-right:10px;'>
            <small style='color: #fbfba8;'>📋 Tarefas Ativas</small>
            <h2 style='color: white; margin: 5px 0 0 0;'>{len(st.session_state.tasks)}</h2>
            <span style='color: #fbfba8; font-size: 0.8rem;'>Kanban atualizado</span>
        </div>
        <div class='dashboard-card' style='flex:1;'>
            <small style='color: #8b9bb4;'>🔬 Eficiência Média</small>
            <h2 style='color: white; margin: 5px 0 0 0;'>92.4%</h2>
            <span style='color: #10b981; font-size: 0.8rem;'>+2.1% hoje</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Model Parameters")
        temp = st.slider("Temperature (K)", 200, 600, 298)
        conc = st.slider("Initial Concentration (M)", 0.1, 10.0, 1.0)
        pressure = st.slider("Pressure (atm)", 0.1, 5.0, 1.0)
        
    with col2:
        tab1, tab2 = st.tabs(["Kinetics", "Thermodynamics"])
        with tab1:
            fig1 = cm.run_model_1_kinetics(temp, conc)
            st.plotly_chart(fig1, use_container_width=True)
        with tab2:
            fig2, dg = cm.run_model_2_thermodynamics(temp)
            st.plotly_chart(fig2, use_container_width=True)
            st.info(f"Current ΔG: {dg:.2f} J/mol")
