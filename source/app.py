import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import json

st.set_page_config(page_title="Simulador", page_icon="🧬")


def dashboard():
    st.markdown("<h1 style='text-align: center; color: orange;'>Simulador</h1>", unsafe_allow_html=True)
    st.text_input('Entre com seu CEP')

dashboard()