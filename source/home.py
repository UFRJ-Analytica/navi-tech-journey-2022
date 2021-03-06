import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import json

from Componentes.Data import collect_data
from Componentes.Form import show_formulario
from Componentes.Cards import show_cards
import Componentes.Utils as Utils

st.set_page_config(page_title="PowerUp", page_icon="💡", layout="wide")


def dashboard():
    collect_data()
    st.markdown(Utils.tooltip_style, unsafe_allow_html=True)

    if 'formulario' not in st.session_state:
        show_formulario()
    else:
        show_cards()


dashboard()
