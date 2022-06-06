import streamlit as st

import Componentes.Utils as Utils
from Componentes.Utils import mustard_yellow, green,white
from Componentes.Optimizer import Option, CurrentOption

def show_introducao():
    st.markdown(f"""
        <h1 style='color: {mustard_yellow};'>
        Simulador Energético
        </h1>""", 
        unsafe_allow_html=True
    )
    st.markdown(f"""
        <p style='color: {white}; font-size: 24px'>
        <b>Simule o quanto você poderia economizar com um mercado livre de energia.</b>
        </p><br><br>""", 
        unsafe_allow_html=True
    )

def show_cards():
    show_introducao()
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.form("CurrentOption"):
            gasto_kwh = Utils.global_state["gasto"]
            atual = CurrentOption(gasto_kwh)
            atual.current_option()
            atual.show_card("Atual Gasto Energético", mustard_yellow)
            st.form_submit_button("Eu Quero!")

    with col2:
        with st.form("Option1"):
            gasto_kwh = Utils.global_state["gasto"]
            atual = Option(0, gasto_kwh)
            atual.optimize_option()
            atual.show_card("Opção 2: Econômico", green)
            st.form_submit_button("Eu Quero!")

    with col3:
        with st.form("Option2"):
            gasto_kwh = Utils.global_state["gasto"]
            atual = Option(1, gasto_kwh)
            atual.optimize_option()
            atual.show_card("Opção 2: Sustentabilidade", green)
            st.form_submit_button("Eu Quero!")
            
    with col4:
        with st.form("Option3"):
            gasto_kwh = Utils.global_state["gasto"]
            atual = Option(0.5, gasto_kwh)
            atual.optimize_option()
            atual.show_card("Opção 3: Equilibrada", green)
            st.form_submit_button("Eu Quero!")