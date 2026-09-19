import streamlit as st
import chemistry_models as cm

def show():
    st.title("🔤 Computational Chemistry Alphabet")
    st.markdown("Explore concepts of computational chemistry from A to Y.")
    
    # Computational Chemistry Alphabet dictionary
    concepts = {
        "A": {"name": "Atom", "icon": "⚛️", "desc": "The basic building block of chemistry and molecular modeling."},
        "B": {"name": "Basis set", "icon": "🎯", "desc": "A set of functions used to create molecular orbitals."},
        "C": {"name": "Contour plot", "icon": "🌀", "desc": "Graphical representation of a 3D surface in 2D using isolines."},
        "D": {"name": "Density plot", "icon": "☁️", "desc": "Visual representation of electron probability distribution."},
        "E": {"name": "Energy surface", "icon": "🎢", "desc": "Potential Energy Surface (PES) mapping energy to molecular geometry."},
        "F": {"name": "Force field", "icon": "🧲", "desc": "Set of parameters and equations used to simulate molecular mechanics."},
        "G": {"name": "Grid", "icon": "🔲", "desc": "Discretized spatial points used in numerical integration and visualization."},
        "H": {"name": "Hamiltonian matrix", "icon": "🔢", "desc": "Operator corresponding to the total energy of the quantum system."},
        "I": {"name": "Isosurface", "icon": "🧊", "desc": "A 3D surface representing points of a constant value within a volume."},
        "J": {"name": "J-coupling", "icon": "🔄", "desc": "Indirect dipole-dipole coupling between nuclear spins in NMR."},
        "K": {"name": "k-space", "icon": "💎", "desc": "Reciprocal space used in solid-state physics for periodic systems."},
        "L": {"name": "LUMO", "icon": "🌸", "desc": "Lowest Unoccupied Molecular Orbital."},
        "M": {"name": "Molecular dynamics", "icon": "🏃‍♂️", "desc": "Computer simulation of physical movements of atoms and molecules."},
        "N": {"name": "Numerical integration", "icon": "🧮", "desc": "Algorithms to calculate numerical approximations of integrals."},
        "O": {"name": "Optimization path", "icon": "📉", "desc": "The trajectory taken by an algorithm to find the minimum energy structure."},
        "P": {"name": "Potential energy curve", "icon": "🛝", "desc": "2D representation of energy vs. interatomic distance."},
        "Q": {"name": "Quantum wavefunction", "icon": "🌊", "desc": "Mathematical description of the quantum state of an isolated system."},
        "R": {"name": "Reaction coordinate diagram", "icon": "📈", "desc": "Shows the energy profile along the path of a chemical reaction."},
        "S": {"name": "Supercomputer", "icon": "🖥️", "desc": "High-performance computing cluster essential for heavy simulations."},
        "T": {"name": "Tight-binding model", "icon": "⛓️", "desc": "Quantum mechanical model to calculate electronic band structure."},
        "U": {"name": "Unit cell", "icon": "📦", "desc": "The smallest repeating unit that makes up a crystal lattice."},
        "V": {"name": "Vibrational frequencies", "icon": "📳", "desc": "Frequencies at which molecules vibrate, related to IR spectroscopy."},
        "W": {"name": "Wannier functions", "icon": "🧬", "desc": "A complete set of orthogonal functions used in solid-state physics."},
        "X": {"name": "XTB", "icon": "✖️", "desc": "Extended Tight-Binding semiempirical quantum chemistry method."},
        "Y": {"name": "Yield", "icon": "✅", "desc": "The amount of product obtained in a chemical reaction."}
    }
    
    st.markdown("### Selecione uma letra:")
    
    letter_keys = list(concepts.keys())
    
    if 'selected_concept_letter' not in st.session_state:
        st.session_state.selected_concept_letter = 'A'
        
    cols = st.columns(8)
    for i, letter in enumerate(letter_keys):
        with cols[i % 8]:
            if st.button(letter, key=f"btn_comp_{letter}"):
                st.session_state.selected_concept_letter = letter
                st.rerun()
                
    selected_letter = st.session_state.get('selected_concept_letter', 'A')
    
    st.divider()
    
    if selected_letter in concepts:
        c = concepts[selected_letter]
        st.markdown(f"""
        <div class='dashboard-card' style='border-color: var(--accent-orange); display: flex; align-items: center; justify-content: space-between;'>
            <div style='flex: 1;'>
                <h1 style='font-size: 5rem; color: var(--accent-orange); margin: 0;'>{selected_letter}</h1>
                <h2 style='margin: 0;'>{c['name']}</h2>
            </div>
            <div style='flex: 2; border-left: 1px solid var(--border-color); padding-left: 20px;'>
                <h1 style='font-size: 4rem; text-align: center;'>{c['icon']}</h1>
                <p><strong>Conceito:</strong> <span class='badge-orange'>{c['name']}</span></p>
                <p><strong>Descrição:</strong> {c['desc']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Map Specific Letters to Workflow Models
        if selected_letter == "R":
            st.divider()
            st.subheader("Simulação Associada: Cinética de Reação")
            col1, col2 = st.columns([1, 2])
            with col1:
                temp = st.slider("Temperatura (K)", 200, 600, 300, key="r_temp")
                conc = st.slider("Concentração Inicial (M)", 0.1, 10.0, 1.0, key="r_conc")
            with col2:
                fig = cm.run_model_1_kinetics(temp, conc)
                st.plotly_chart(fig, use_container_width=True)

        elif selected_letter == "E":
            st.divider()
            st.subheader("Simulação Associada: Energia Livre de Gibbs (Termodinâmica)")
            col1, col2 = st.columns([1, 2])
            with col1:
                temp = st.slider("Temperatura Atual (K)", 200, 600, 298, key="e_temp")
            with col2:
                fig, dg = cm.run_model_2_thermodynamics(temp)
                st.plotly_chart(fig, use_container_width=True)
                if dg < 0:
                    st.success(f"Reação Espontânea! ΔG = {dg:.2f} J/mol")
                else:
                    st.error(f"Reação Não-Espontânea. ΔG = {dg:.2f} J/mol")

        elif selected_letter == "Y":
            st.divider()
            st.subheader("Simulação Associada: Superfície de Previsão de Rendimento")
            col1, col2 = st.columns([1, 2])
            with col1:
                temp = st.slider("Temperatura Otimizada (K)", 200, 600, 350, key="y_temp")
                pressure = st.slider("Pressão (atm)", 0.1, 5.0, 2.0, key="y_press")
            with col2:
                fig, yield_pct = cm.run_model_3_yield_prediction(temp, pressure)
                st.plotly_chart(fig, use_container_width=True)
                st.metric("Rendimento Previsto", f"{yield_pct:.1f}%")

        elif selected_letter == "A":
            st.divider()
            st.subheader("Simulação Associada: Curva de Titulação Ácido-Base")
            col1, col2 = st.columns([1, 2])
            with col1:
                volume = st.slider("Volume de Base Adicionado (mL)", 0.0, 50.0, 20.0, key="a_vol")
                conc_acid = st.number_input("Concentração do Ácido Forte (M)", 0.01, 1.0, 0.1, key="a_acid")
                conc_base = st.number_input("Concentração da Base Forte (M)", 0.01, 1.0, 0.1, key="a_base")
            with col2:
                fig, ph = cm.run_model_4_titration(volume, conc_acid, conc_base)
                st.plotly_chart(fig, use_container_width=True)
                st.metric("pH Atual", f"{ph:.2f}")

        elif selected_letter == "M":
            st.divider()
            st.subheader("Simulação Associada: Cinética Enzimática (Michaelis-Menten)")
            col1, col2 = st.columns([1, 2])
            with col1:
                vmax = st.slider("Vmax (μM/s)", 10, 100, 50, key="m_vmax")
                km = st.slider("Constante de Michaelis Km (μM)", 1, 50, 10, key="m_km")
                s_conc = st.slider("Concentração do Substrato [S] (μM)", 0, 100, 20, key="m_s")
            with col2:
                fig, v0 = cm.run_model_5_michaelis_menten(vmax, km, s_conc)
                st.plotly_chart(fig, use_container_width=True)
                st.metric("Velocidade (v0)", f"{v0:.2f} μM/s")

        elif selected_letter == "T":
            st.divider()
            st.subheader("Simulação Associada: Gráfico de Arrhenius (Energia de Ativação)")
            col1, col2 = st.columns([1, 2])
            with col1:
                ea = st.slider("Energia de Ativação Ea (kJ/mol)", 10, 150, 50, key="t_ea")
            with col2:
                fig = cm.run_model_6_arrhenius(ea)
                st.plotly_chart(fig, use_container_width=True)

