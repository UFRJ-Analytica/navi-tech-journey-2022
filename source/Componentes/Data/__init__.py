import streamlit as st
import pandas as pd
import requests
import Componentes.Utils as Utils

empresas = {
    "Light SA": "60444437000146",
    "Enel RJ": "33050071000158"
}

def collect_data():
    Utils.global_state["tarifas_distribuidoras"] = pd.read_csv("../dados/TarifasDistribuidoras.csv")
    Utils.global_state["dados_leilao"] = pd.read_csv("../dados/ConsolidadoVendedoresLeilao.csv", sep=';', encoding='mbcs')