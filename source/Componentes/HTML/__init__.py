import streamlit as st

def _mount_card_title(cor,title,final_cost):
    st.markdown(f"""
        <p style='color: {cor}; font-size: 20px; text-align: center'>
        <b>{title}</b>
        </p>""", 
        unsafe_allow_html=True
    )
    st.markdown(f"""
        <p style='color: {cor}; font-size: 40px; text-align: center'>
        <b>R$ {final_cost}/mês</b>
        </p>""", 
        unsafe_allow_html=True
    )

def _mount_card_rows(cor,dict_data, has_tooltips=False):
    
    dict_tooltip = {
        "Geração": "Precisa ser pago a quem vai 'criar' a energia",
        "Transmissão": "Precisa ser pago a quem vai levar a energia gerada as cidades",
        "Distribuição": "Precisa ser pago a quem vai levar das cidades para o seu lar",
        "Encargos": "São taxas usadas para manter iniciativas do governo,",
        "Impostos": "Impostos como ICMS, PIS/PASEP e COFINS fazem parte desse valor",

        "Tarifa de Energia": "Tarifa necessária para pagar a 'criação' da energia + uns impostos aí",
        "Tarifa de Uso do Sistema de Distribuição": "Tarifa necessária para pagar a quem vai levar a energia para o seu lar",
    }

    for i in dict_data.keys():
        if i == "Outros":
            _mount_card_row(cor,i,dict_data[i], has_tooltip=False)
        else:
            _mount_card_row(cor,i,dict_data[i], has_tooltip=has_tooltips,tooltip_text=dict_tooltip[i])

def _mount_card_row(color, text, value, has_tooltip=False, tooltip_text=""):
    if has_tooltip:
        st.markdown(f"""<p style='color: {color}; font-size: 16px;'>
                            <b class="tooltip" data-text="{tooltip_text}">{text}: R$ {value}</b>
                        </p>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""<p style='color: {color}; font-size: 16px;'>
                            <b>{text}: R$ {value}</b>
                        </p>""", unsafe_allow_html=True)