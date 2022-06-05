import streamlit as st
from Componentes.Utils import dark_blue, pink
from Componentes.Data import empresas

def show_introducao():
    st.markdown(f"""
        <h1 style='color: {pink};'>
        Simulador Energético
        </h1>""", 
        unsafe_allow_html=True
    )
    st.markdown(f"""
        <p style='color: {dark_blue}; font-size: 24px'>
        <b>Simule o quanto você poderia economizar com um mercado livre de energia.</b>
        </p><br><br>""", 
        unsafe_allow_html=True
    )

def show_formulario():
    show_introducao()
    
    with st.form("FormularioInicial"):
        st.markdown(f"""
            <p style='color: {dark_blue}; font-size: 18px'>
            <b>Conte para a gente um pouco sobre você:</b>
            </p>""", 
            unsafe_allow_html=True
        )

        distribuidora = st.selectbox("Distribuidora Atual", empresas.keys())
        gasto = st.number_input('Gasto de Energia Mensal em kWh')

        submitted = st.form_submit_button("Realizar Simulação")
        if submitted:
            st.session_state["formulario"] = True
            st.experimental_rerun()
