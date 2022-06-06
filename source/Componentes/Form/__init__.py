import streamlit as st

import Componentes.Utils as Utils
from Componentes.Utils import purple_black, mustard_yellow, white

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

    with st.expander("Você conhece o Mercado de Livre Energia"):
        st.write(f"""
            O Mercado Livre de Energia é um ambiente de negociação de energia elétrica em que o consumidor pode escolher de onde comprar a eletricidade que consumirá, privilegiando a empresa que melhor atenda às suas expectativas de custo e benefício. 
            Diferente do Mercado Cativo, formado pelos consumidores que têm acesso à energia com tarifas estabelecidas pelo governo, do qual você faz parte, no Mercado Livre você pode exercer seu poder de escolha e economizar de 10% a 20% na conta de luz, além de ser isento da cobrança de Bandeiras Tarifárias e ainda poder contribuir para o uso mais sustentável da energia.""")

def show_formulario():
    show_introducao()
    
    with st.form("FormularioInicial"):
        st.markdown(f"""
            <p style='color: {white}; font-size: 18px'>
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
