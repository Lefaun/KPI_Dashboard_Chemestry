import numpy as np
import plotly.graph_objects as go

def get_alphabet_visualization(letter):
    """Returns a Plotly Figure for a given letter A-Y representing a chemistry concept."""
    fig = go.Figure()
    
    # Common layout settings for the card
    layout_settings = dict(
        template="plotly_white",
        margin=dict(l=10, r=10, t=30, b=10),
        height=300
    )

    if letter == "A":  # Atom (3D Scatter)
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = 10 * np.outer(np.cos(u), np.sin(v))
        y = 10 * np.outer(np.sin(u), np.sin(v))
        z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
        fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='markers', marker=dict(size=15, color='#ef4444'), name='Nucleus'))
        
        # Electron cloud (random points in sphere)
        r = 10 * np.random.rand(200)**(1/3.)
        theta = np.arccos(2 * np.random.rand(200) - 1)
        phi = 2 * np.pi * np.random.rand(200)
        ex = r * np.sin(theta) * np.cos(phi)
        ey = r * np.sin(theta) * np.sin(phi)
        ez = r * np.cos(theta)
        fig.add_trace(go.Scatter3d(x=ex, y=ey, z=ez, mode='markers', marker=dict(size=3, color='#0ea5e9', opacity=0.5), name='Electron Cloud'))
        fig.update_layout(**layout_settings, title="Atom Model")

    elif letter == "B":  # Basis set
        x = np.linspace(-5, 5, 100)
        slater = np.exp(-abs(x))
        gaussian = np.exp(-x**2)
        fig.add_trace(go.Scatter(x=x, y=slater, name='Slater Type (STO)', line=dict(color='#ef4444')))
        fig.add_trace(go.Scatter(x=x, y=gaussian, name='Gaussian Type (GTO)', line=dict(color='#0ea5e9', dash='dash')))
        fig.update_layout(**layout_settings, title="Basis Set Functions")

    elif letter == "C":  # Contour plot
        x = np.linspace(-3, 3, 50)
        y = np.linspace(-3, 3, 50)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(X) * np.cos(Y)
        fig.add_trace(go.Contour(z=Z, x=x, y=y, colorscale='Viridis'))
        fig.update_layout(**layout_settings, title="Contour Plot")

    elif letter == "D":  # Density plot
        x = np.random.randn(1000)
        y = np.random.randn(1000)
        fig.add_trace(go.Histogram2dContour(x=x, y=y, colorscale='Blues', reversescale=True))
        fig.update_layout(**layout_settings, title="Electron Density Plot")

    elif letter == "E":  # Energy surface
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))
        fig.add_trace(go.Surface(z=Z, x=x, y=y, colorscale='Plasma'))
        fig.update_layout(**layout_settings, title="Potential Energy Surface")

    elif letter == "F":  # Force field
        fig.add_trace(go.Scatter3d(x=[0, 1, 2], y=[0, 1, 0], z=[0, 0, 0], mode='lines+markers', 
                                   marker=dict(size=10, color='#10b981'), line=dict(width=5, color='#cbd5e1')))
        fig.update_layout(**layout_settings, title="Force Field (Springs & Masses)")

    elif letter == "G":  # Grid
        x = np.linspace(-2, 2, 5)
        y = np.linspace(-2, 2, 5)
        z = np.linspace(-2, 2, 5)
        X, Y, Z = np.meshgrid(x, y, z)
        fig.add_trace(go.Scatter3d(x=X.flatten(), y=Y.flatten(), z=Z.flatten(), mode='markers', 
                                   marker=dict(size=3, color='#94a3b8')))
        fig.update_layout(**layout_settings, title="Discretized Grid")

    elif letter == "H":  # Hamiltonian matrix
        matrix = np.random.rand(10, 10)
        matrix = (matrix + matrix.T)/2 # Make it symmetric (Hermitian-like)
        np.fill_diagonal(matrix, np.random.rand(10) * 5) # Larger diagonal (energies)
        fig.add_trace(go.Heatmap(z=matrix, colorscale='Inferno'))
        fig.update_layout(**layout_settings, title="Hamiltonian Matrix")

    elif letter == "I":  # Isosurface (Simulated with 3D Mesh)
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))
        fig.add_trace(go.Surface(x=x, y=y, z=z, opacity=0.5, colorscale='Teal'))
        fig.update_layout(**layout_settings, title="Isosurface Volume")

    elif letter == "J":  # J-coupling
        freqs = np.linspace(0, 10, 500)
        intensity = np.exp(-((freqs - 3.0)**2)/0.01) + 0.5*np.exp(-((freqs - 3.2)**2)/0.01) + np.exp(-((freqs - 7.0)**2)/0.01)
        fig.add_trace(go.Scatter(x=freqs, y=intensity, mode='lines', line=dict(color='#0284c7')))
        fig.update_layout(**layout_settings, title="NMR J-Coupling Spectrum")

    elif letter == "K":  # k-space
        pts = np.random.randn(300, 3) * 0.5
        fig.add_trace(go.Scatter3d(x=pts[:,0], y=pts[:,1], z=pts[:,2], mode='markers', marker=dict(size=4, color=pts[:,2], colorscale='Viridis')))
        fig.update_layout(**layout_settings, title="k-Space Reciprocal Lattice")

    elif letter == "L":  # LUMO
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))
        # Modify shape to look like p-orbital lobe
        z = z * np.abs(z) * 2
        fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='RdBu'))
        fig.update_layout(**layout_settings, title="Lowest Unoccupied Molecular Orbital (LUMO)")

    elif letter == "M":  # Molecular dynamics
        time = np.arange(0, 1000)
        temp = 300 + 10 * np.random.randn(1000).cumsum() * 0.1
        fig.add_trace(go.Scatter(x=time, y=temp, mode='lines', line=dict(color='#f59e0b', width=1)))
        fig.update_layout(**layout_settings, title="MD Trajectory (Temperature Fluctuation)")

    elif letter == "N":  # Numerical integration
        x = np.linspace(0, 5, 20)
        y = np.sin(x) + 2
        fig.add_trace(go.Bar(x=x, y=y, opacity=0.6, marker_color='#3b82f6', name='Integration Bars'))
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#1e40af', width=3), name='Function'))
        fig.update_layout(**layout_settings, title="Numerical Integration (Trapezoidal Rule)")

    elif letter == "O":  # Optimization path
        x = np.linspace(-2, 2, 50)
        y = np.linspace(-2, 2, 50)
        X, Y = np.meshgrid(x, y)
        Z = X**2 + Y**2
        fig.add_trace(go.Contour(x=x, y=y, z=Z, colorscale='Greys', showscale=False))
        # Path
        px = [1.8, 1.0, 0.5, 0.2, 0.0]
        py = [1.5, 0.8, 0.3, 0.1, 0.0]
        fig.add_trace(go.Scatter(x=px, y=py, mode='lines+markers', line=dict(color='#ef4444', width=3), marker=dict(size=8), name='Path'))
        fig.update_layout(**layout_settings, title="Geometry Optimization Path")

    elif letter == "P":  # Potential energy curve
        r = np.linspace(0.5, 5, 100)
        De = 5.0
        re = 1.0
        a = 1.5
        V = De * (1 - np.exp(-a*(r - re)))**2
        fig.add_trace(go.Scatter(x=r, y=V, mode='lines', line=dict(color='#8b5cf6', width=3)))
        fig.update_layout(**layout_settings, title="Morse Potential Energy Curve")

    elif letter == "Q":  # Quantum wavefunction
        x = np.linspace(-5, 5, 200)
        psi = np.exp(-x**2/2) * np.cos(5*x) # Simple wave packet
        prob = psi**2
        fig.add_trace(go.Scatter(x=x, y=psi, name='Wavefunction ψ', line=dict(color='#3b82f6')))
        fig.add_trace(go.Scatter(x=x, y=prob, name='Probability |ψ|²', line=dict(color='#f43f5e', fill='tozeroy')))
        fig.update_layout(**layout_settings, title="Quantum Wavefunction & Probability")

    elif letter == "R":  # Reaction coordinate diagram
        rc = np.linspace(0, 10, 100)
        E = 10 * np.exp(-(rc-5)**2/2) + rc # Barrier + exothermicity
        fig.add_trace(go.Scatter(x=rc, y=E, mode='lines', line=dict(color='#14b8a6', width=3)))
        fig.update_layout(**layout_settings, title="Reaction Coordinate Profile")

    elif letter == "S":  # Supercomputer
        nodes = np.random.rand(20, 2)
        fig.add_trace(go.Scatter(x=nodes[:,0], y=nodes[:,1], mode='markers', marker=dict(size=15, color='#3b82f6')))
        # Connect nodes to simulate network
        for i in range(10):
            fig.add_trace(go.Scatter(x=[nodes[i,0], nodes[i+1,0]], y=[nodes[i,1], nodes[i+1,1]], mode='lines', line=dict(color='#cbd5e1')))
        fig.update_layout(**layout_settings, title="HPC Compute Node Topology", showlegend=False)

    elif letter == "T":  # Tight-binding model
        k = np.linspace(-np.pi, np.pi, 100)
        E1 = -2 * np.cos(k)
        E2 = 2 * np.cos(k) + 4
        fig.add_trace(go.Scatter(x=k, y=E1, mode='lines', line=dict(color='#475569', width=2), name='Valence Band'))
        fig.add_trace(go.Scatter(x=k, y=E2, mode='lines', line=dict(color='#ef4444', width=2), name='Conduction Band'))
        fig.update_layout(**layout_settings, title="Tight-Binding Band Structure")

    elif letter == "U":  # Unit cell
        # Simple cube lattice
        pts = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[1,1,1],[0,1,1]])
        fig.add_trace(go.Scatter3d(x=pts[:,0], y=pts[:,1], z=pts[:,2], mode='markers', marker=dict(size=12, color='#f59e0b')))
        fig.update_layout(**layout_settings, title="Crystal Unit Cell")

    elif letter == "V":  # Vibrational
        wavenumber = np.linspace(500, 4000, 500)
        transmittance = 100 - (50*np.exp(-((wavenumber-1700)/20)**2) + 80*np.exp(-((wavenumber-3000)/50)**2))
        fig.add_trace(go.Scatter(x=wavenumber, y=transmittance, mode='lines', line=dict(color='#0f766e')))
        fig.update_layout(**layout_settings, title="Vibrational (IR) Spectrum", xaxis=dict(autorange="reversed"))

    elif letter == "W":  # Wannier
        x = np.linspace(-5, 5, 100)
        w = np.sinc(x) * np.exp(-abs(x)*0.2)
        fig.add_trace(go.Scatter(x=x, y=w, mode='lines', line=dict(color='#8b5cf6', fill='tozeroy')))
        fig.update_layout(**layout_settings, title="Localized Wannier Function")

    elif letter == "X":  # XTB
        methods = ['AM1', 'PM3', 'DFTB', 'GFN-xTB', 'DFT']
        accuracy = [5, 6, 7, 9, 10]
        fig.add_trace(go.Bar(x=methods, y=accuracy, marker_color=['#94a3b8', '#94a3b8', '#94a3b8', '#10b981', '#cbd5e1']))
        fig.update_layout(**layout_settings, title="Semiempirical Methods (Accuracy)")

    elif letter == "Y":  # Yield
        methods = ['Batch 1', 'Batch 2', 'Batch 3', 'Batch 4']
        yields = [85, 92, 78, 95]
        fig.add_trace(go.Bar(x=methods, y=yields, marker_color='#f97316'))
        fig.update_layout(**layout_settings, title="Reaction Yield by Batch")

    return fig
