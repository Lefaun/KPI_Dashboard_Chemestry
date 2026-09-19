import streamlit as st

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
