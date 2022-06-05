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

def show_cards():
    show_introducao()
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.form("CurrentOption"):
            st.markdown(f"""
                <p style='color: {dark_blue}; font-size: 20px; text-align: center'>
                <b>Atual Gasto Energético</b>
                </p>""", 
                unsafe_allow_html=True
            )
            st.markdown(f"""
                <p style='color: {dark_blue}; font-size: 40px; text-align: center'>
                <b>R$ 300/mês</b>
                </p>""", 
                unsafe_allow_html=True
            )

            st.markdown(f"<p style='color: {dark_blue}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {dark_blue}; font-size: 16px;'><b>Geração: R$ 176.86</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {dark_blue}; font-size: 16px;'><b>Transmissão: R$ 12.70</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {dark_blue}; font-size: 16px;'><b>Distribuição: R$ 68.17</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {dark_blue}; font-size: 16px;'><b>Encargos: R$ 42.17</b></p>", unsafe_allow_html=True)

            st.markdown(f"<p style='color: {dark_blue}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {dark_blue}; font-size: 16px;'><b>Light S.A. - Distribuidora</b></p>", unsafe_allow_html=True)

            st.form_submit_button("Eu Quero!")

    with col2:
        with st.form("Option1"):
            st.markdown(f"""
                <p style='color: {pink}; font-size: 20px; text-align: center'>
                <b>Opção 1: Econômica</b>
                </p>""", 
                unsafe_allow_html=True
            )
            st.markdown(f"""
                <p style='color: {pink}; font-size: 40px; text-align: center'>
                <b>R$ 300/mês</b>
                </p>""", 
                unsafe_allow_html=True
            )
            
            st.markdown(f"<p style='color: {pink}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Geração: R$ 176.86</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Transmissão: R$ 12.70</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Distribuição: R$ 68.17</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Encargos: R$ 42.17</b></p>", unsafe_allow_html=True)

            st.markdown(f"<p style='color: {pink}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Light S.A. - Distribuidora</b></p>", unsafe_allow_html=True)
            st.form_submit_button("Eu Quero!")

    with col3:
        with st.form("Option2"):
            st.markdown(f"""
                <p style='color: {pink}; font-size: 20px; text-align: center'>
                <b>Opção 2: Sustentabilidade</b>
                </p>""", 
                unsafe_allow_html=True
            )
            st.markdown(f"""
                <p style='color: {pink}; font-size: 40px; text-align: center'>
                <b>R$ 300/mês</b>
                </p>""", 
                unsafe_allow_html=True
            )
            
            st.markdown(f"<p style='color: {pink}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Geração: R$ 176.86</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Transmissão: R$ 12.70</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Distribuição: R$ 68.17</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Encargos: R$ 42.17</b></p>", unsafe_allow_html=True)

            st.markdown(f"<p style='color: {pink}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Light S.A. - Distribuidora</b></p>", unsafe_allow_html=True)
            st.form_submit_button("Eu Quero!")
            
    with col4:
        with st.form("Option3"):
            st.markdown(f"""
                <p style='color: {pink}; font-size: 20px; text-align: center'>
                <b>Opção 3: Equilibrada</b>
                </p>""", 
                unsafe_allow_html=True
            )
            st.markdown(f"""
                <p style='color: {pink}; font-size: 40px; text-align: center'>
                <b>R$ 300/mês</b>
                </p>""", 
                unsafe_allow_html=True
            )
            
            st.markdown(f"<p style='color: {pink}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Geração: R$ 176.86</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Transmissão: R$ 12.70</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Distribuição: R$ 68.17</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Encargos: R$ 42.17</b></p>", unsafe_allow_html=True)

            st.markdown(f"<p style='color: {pink}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {pink}; font-size: 16px;'><b>Light S.A. - Distribuidora</b></p>", unsafe_allow_html=True)
            st.form_submit_button("Eu Quero!")