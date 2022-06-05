import streamlit as st

import Componentes.Utils as Utils
from Componentes.Utils import dark_blue, pink

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

        empresas = Utils.global_state["tarifas_distribuidoras"]["SigAgente"].values
        Utils.global_state["distribuidora"] = st.selectbox("Distribuidora Atual", empresas)
        Utils.global_state["gasto"] = st.number_input('Gasto de Energia Mensal em kWh')

        submitted = st.form_submit_button("Realizar Simulação")
        if submitted:
            st.session_state["formulario"] = True
            st.experimental_rerun()
