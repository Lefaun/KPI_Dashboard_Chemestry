import streamlit as st
import chemistry_models as cm

def show():
    st.title("📊 Galeria de Infográficos Químicos")
    st.markdown("Explore modelos químicos interativos através de gráficos e simuladores dinâmicos.")
    
    # Selection of the model
    model_choice = st.selectbox(
        "Selecione um Modelo Químico:",
        [
            "1. Cinética de Reação de 1ª Ordem",
            "2. Termodinâmica & Energia Livre de Gibbs",
            "3. Superfície de Previsão de Rendimento",
            "4. Curva de Titulação Ácido-Base",
            "5. Cinética Enzimática (Michaelis-Menten)",
            "6. Gráfico de Arrhenius (Energia de Ativação)"
        ]
    )
    
    st.divider()
    
    col_params, col_graph = st.columns([1, 2])
    
    if "1. Cinética" in model_choice:
        with col_params:
            st.subheader("⚙️ Parâmetros (Cinética)")
            temp = st.slider("Temperatura (K)", 200, 600, 300)
            conc = st.slider("Concentração Inicial (M)", 0.1, 10.0, 1.0)
            st.info("Simula o decaimento de um reagente A e a formação de um produto B com base na temperatura.")
        with col_graph:
            fig = cm.run_model_1_kinetics(temp, conc)
            st.plotly_chart(fig, use_container_width=True)
            
    elif "2. Termodinâmica" in model_choice:
        with col_params:
            st.subheader("⚙️ Parâmetros (Termodinâmica)")
            temp = st.slider("Temperatura Atual (K)", 200, 600, 298)
            st.info("Calcula se a reação é espontânea (ΔG < 0) à temperatura atual.")
        with col_graph:
            fig, dg = cm.run_model_2_thermodynamics(temp)
            st.plotly_chart(fig, use_container_width=True)
            if dg < 0:
                st.success(f"Reação Espontânea! ΔG = {dg:.2f} J/mol")
            else:
                st.error(f"Reação Não-Espontânea. ΔG = {dg:.2f} J/mol")
                
    elif "3. Superfície" in model_choice:
        with col_params:
            st.subheader("⚙️ Parâmetros (Rendimento)")
            temp = st.slider("Temperatura Otimizada (K)", 200, 600, 350)
            pressure = st.slider("Pressão (atm)", 0.1, 5.0, 2.0)
            st.info("Mapa de contorno 2D para identificar o 'sweet spot' de rendimento de um processo produtivo.")
        with col_graph:
            fig, yield_pct = cm.run_model_3_yield_prediction(temp, pressure)
            st.plotly_chart(fig, use_container_width=True)
            st.metric("Rendimento Previsto", f"{yield_pct:.1f}%")
            
    elif "4. Titulação" in model_choice:
        with col_params:
            st.subheader("⚙️ Parâmetros (Titulação)")
            volume = st.slider("Volume de Base Adicionado (mL)", 0.0, 50.0, 20.0)
            conc_acid = st.number_input("Concentração do Ácido Forte (M)", 0.01, 1.0, 0.1)
            conc_base = st.number_input("Concentração da Base Forte (M)", 0.01, 1.0, 0.1)
            st.info("Curva clássica de titulação, prevê o pH em função do volume de titulante.")
        with col_graph:
            fig, ph = cm.run_model_4_titration(volume, conc_acid, conc_base)
            st.plotly_chart(fig, use_container_width=True)
            st.metric("pH Atual", f"{ph:.2f}")
            
    elif "5. Cinética Enzimática" in model_choice:
        with col_params:
            st.subheader("⚙️ Parâmetros (Michaelis-Menten)")
            vmax = st.slider("Vmax (μM/s)", 10, 100, 50)
            km = st.slider("Constante de Michaelis Km (μM)", 1, 50, 10)
            s_conc = st.slider("Concentração do Substrato [S] (μM)", 0, 100, 20)
            st.info("Prevê a velocidade de uma reação catalisada por enzimas.")
        with col_graph:
            fig, v0 = cm.run_model_5_michaelis_menten(vmax, km, s_conc)
            st.plotly_chart(fig, use_container_width=True)
            st.metric("Velocidade (v0)", f"{v0:.2f} μM/s")
            
    elif "6. Gráfico de Arrhenius" in model_choice:
        with col_params:
            st.subheader("⚙️ Parâmetros (Arrhenius)")
            ea = st.slider("Energia de Ativação Ea (kJ/mol)", 10, 150, 50)
            st.info("Demonstra a relação linear entre o logaritmo da constante de velocidade (ln k) e o inverso da temperatura (1/T).")
        with col_graph:
            fig = cm.run_model_6_arrhenius(ea)
            st.plotly_chart(fig, use_container_width=True)
