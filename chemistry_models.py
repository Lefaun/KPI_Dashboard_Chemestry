import numpy as np
import plotly.graph_objects as go

def run_model_1_kinetics(temp, concentration):
    """Model 1: Reaction Kinetics Simulator"""
    time = np.linspace(0, 100, 100)
    # k depends on temperature (Arrhenius-like relation)
    k = 0.05 * np.exp(-1000 / (8.314 * temp))
    conc = concentration * np.exp(-k * time)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=conc, mode='lines', name='Concentration [A]', line=dict(color='#0ea5e9', width=3)))
    
    # Add product concentration assuming A -> B
    prod = concentration - conc
    fig.add_trace(go.Scatter(x=time, y=prod, mode='lines', name='Product [B]', line=dict(color='#f97316', width=3)))
    
    fig.update_layout(title="Cinética de Reação de 1ª Ordem", xaxis_title="Tempo (s)", yaxis_title="Concentração (M)",
                      template="plotly_white", plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor="rgba(0,0,0,0)")
    return fig

def run_model_2_thermodynamics(temp):
    """Model 2: Gibbs Free Energy"""
    delta_h = -50000  # J/mol (Exothermic)
    delta_s = -100    # J/(mol*K)
    delta_g = delta_h - temp * delta_s
    
    temps = np.linspace(200, 600, 100)
    dgs = delta_h - temps * delta_s
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=temps, y=dgs, mode='lines', name='ΔG (Energia de Gibbs)', line=dict(color='#10b981', width=3)))
    
    fig.add_vline(x=temp, line_dash="dash", line_color="#ef4444", annotation_text="Temp. Atual")
    fig.add_hline(y=0, line_dash="solid", line_color="#64748b")
    fig.update_layout(title="Energia Livre de Gibbs vs Temperatura", xaxis_title="Temperatura (K)", yaxis_title="ΔG (J/mol)",
                      template="plotly_white", plot_bgcolor="rgba(255,255,255,1)", paper_bgcolor="rgba(0,0,0,0)")
    return fig, delta_g

def run_model_3_yield_prediction(temp, pressure):
    """Model 3: Yield Prediction Contour"""
    t_vals = np.linspace(200, 600, 50)
    p_vals = np.linspace(0.1, 5.0, 50)
    T, P = np.meshgrid(t_vals, p_vals)
    
    # Fake yield function maximized at 400K and 3 atm
    Z = np.clip(100 - ((T - 400)**2)*0.005 - ((P - 3)**2)*15, 0, 100)
    
    fig = go.Figure(data=go.Contour(
        x=t_vals, y=p_vals, z=Z,
        colorscale='Viridis',
        contours=dict(showlabels=True, labelfont=dict(size=12, color='white'))
    ))
    
    # Plot current point
    fig.add_trace(go.Scatter(x=[temp], y=[pressure], mode='markers', marker=dict(color='red', size=12, symbol='star'), name='Parâmetros Atuais'))
    
    fig.update_layout(title="Superfície de Rendimento do Processo", xaxis_title="Temperatura (K)", yaxis_title="Pressão (atm)",
                      template="plotly_white")
    current_yield = np.clip(100 - ((temp - 400)**2)*0.005 - ((pressure - 3)**2)*15, 0, 100)
    return fig, current_yield

def run_model_4_titration(volume, conc_acid, conc_base):
    """Model 4: Acid-Base Titration Curve (Strong Acid + Strong Base)"""
    v_vals = np.linspace(0, 50, 100)
    v_acid = 25.0 # Fixed initial volume of acid
    
    moles_acid = conc_acid * v_acid
    moles_base = conc_base * v_vals
    
    pH_vals = []
    for v_b in v_vals:
        mol_a = conc_acid * v_acid
        mol_b = conc_base * v_b
        total_v = v_acid + v_b
        
        if mol_a > mol_b:
            # Acid in excess
            conc_h = (mol_a - mol_b) / total_v
            pH = -np.log10(conc_h)
        elif mol_b > mol_a:
            # Base in excess
            conc_oh = (mol_b - mol_a) / total_v
            pOH = -np.log10(conc_oh)
            pH = 14 - pOH
        else:
            pH = 7.0
        pH_vals.append(pH)
        
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=v_vals, y=pH_vals, mode='lines', name='Curva de Titulação', line=dict(color='#8b5cf6', width=3)))
    
    # Mark user volume
    # Find closest volume in the array to get its pH
    idx = (np.abs(v_vals - volume)).argmin()
    current_pH = pH_vals[idx]
    
    fig.add_trace(go.Scatter(x=[volume], y=[current_pH], mode='markers', marker=dict(color='red', size=10), name='Ponto Atual'))
    fig.add_hline(y=7, line_dash="dash", line_color="#cbd5e1")
    
    fig.update_layout(title="Curva de Titulação (Ácido Forte vs Base Forte)", xaxis_title="Volume de Base (mL)", yaxis_title="pH",
                      template="plotly_white", yaxis_range=[0, 14])
    return fig, current_pH

def run_model_5_michaelis_menten(vmax, km, s_conc):
    """Model 5: Enzyme Kinetics (Michaelis-Menten)"""
    s_vals = np.linspace(0, 100, 100)
    v0_vals = (vmax * s_vals) / (km + s_vals)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=s_vals, y=v0_vals, mode='lines', name='Velocidade (v0)', line=dict(color='#f43f5e', width=3)))
    
    # Asymptote for Vmax
    fig.add_hline(y=vmax, line_dash="dash", line_color="#cbd5e1", annotation_text="Vmax")
    
    # Current point
    current_v = (vmax * s_conc) / (km + s_conc)
    fig.add_trace(go.Scatter(x=[s_conc], y=[current_v], mode='markers', marker=dict(color='black', size=10), name='Ensaio Atual'))
    
    fig.update_layout(title="Cinética Enzimática de Michaelis-Menten", xaxis_title="Concentração de Substrato [S] (μM)", yaxis_title="Velocidade Inicial (v0)",
                      template="plotly_white")
    return fig, current_v

def run_model_6_arrhenius(activation_energy):
    """Model 6: Arrhenius Plot (ln k vs 1/T)"""
    # E_a in kJ/mol -> convert to J/mol
    Ea_J = activation_energy * 1000
    R = 8.314
    A = 1e10 # Pre-exponential factor
    
    temps = np.linspace(250, 800, 100)
    inv_T = 1 / temps
    ln_k = np.log(A) - (Ea_J / (R * temps))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=inv_T, y=ln_k, mode='lines', name='Gráfico de Arrhenius', line=dict(color='#3b82f6', width=3)))
    
    fig.update_layout(title="Gráfico de Arrhenius", xaxis_title="1 / T (K^-1)", yaxis_title="ln(k)",
                      template="plotly_white")
    return fig

def generate_spc_chart():
    """Generates Statistical Process Control Chart"""
    samples = 50
    data = np.random.normal(100, 5, samples)
    mean = np.mean(data)
    std = np.std(data)
    
    ucl = mean + 3 * std
    lcl = mean - 3 * std
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=data, mode='lines+markers', name='Rendimento', line=dict(color='#0ea5e9')))
    fig.add_hline(y=mean, line_dash="dash", line_color="#64748b", annotation_text="Média")
    fig.add_hline(y=ucl, line_dash="solid", line_color="#ef4444", annotation_text="LSC")
    fig.add_hline(y=lcl, line_dash="solid", line_color="#ef4444", annotation_text="LIC")
    fig.update_layout(title="Cartão de Controlo SPC (Rendimento de Lote)", xaxis_title="Lote", yaxis_title="Rendimento (%)",
                      template="plotly_white")
    return fig
