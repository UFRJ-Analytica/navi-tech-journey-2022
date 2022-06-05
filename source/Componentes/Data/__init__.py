import streamlit as st
import pandas as pd
import requests
import Componentes.Utils as Utils


def collect_data():
    Utils.global_state["precos_leilao"] = pd.read_csv("../dados/PrecoLeiloes.csv")
    Utils.global_state["info_geradoras"] = pd.read_csv("../dados/InfoGeradoras.csv")
    Utils.global_state["tarifas_distribuidoras"] = pd.read_csv("../dados/TarifasDistribuidoras.csv")
