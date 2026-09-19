import streamlit as st

def show():
    st.title("🛒 R&D Services Shop")
    st.markdown("Order reagents, computational time, or lab equipment.")
    
    products = [
        {"id": 1, "name": "Premium Lab Reagent Kit", "price": 499.99, "icon": "🧪"},
        {"id": 2, "name": "HPC Simulation Hours (100h)", "price": 299.00, "icon": "💻"},
        {"id": 3, "name": "Spectrometer Calibration", "price": 150.00, "icon": "🔬"}
    ]
    
    cols = st.columns(3)
    for idx, p in enumerate(products):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class='dashboard-card'>
                <h1 style='text-align:center;'>{p['icon']}</h1>
                <h4 style='text-align:center; color:white;'>{p['name']}</h4>
                <h3 style='text-align:center; color:var(--accent-cyan);'>${p['price']}</h3>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Add to Cart", key=f"add_{p['id']}"):
                st.session_state.cart.append(p)
                st.success(f"Added {p['name']} to cart!")
                
    st.divider()
    st.subheader(f"Shopping Cart ({len(st.session_state.cart)} items)")
    total = sum([item['price'] for item in st.session_state.cart])
    
    for item in st.session_state.cart:
        st.markdown(f"- {item['name']}: **${item['price']}**")
        
    st.markdown(f"### Total: <span style='color:var(--accent-orange);'>${total:.2f}</span>", unsafe_allow_html=True)
    if st.session_state.cart and st.button("Checkout"):
        st.session_state.cart = []
        st.balloons()
        st.success("Order placed successfully!")
