import streamlit as st
import pandas as pd
import cvxpy as cp
import numpy as np

import Componentes.Utils as Utils
from Componentes.Utils import dark_blue, pink

class Option:
    def __init__(self, k_sustentabilidade, gasto_kwh):
        self.k_sustentabilidade = k_sustentabilidade
        self.gasto_kwh = gasto_kwh

    def optimize_option(self):
        """ Optimization:
        
            min z = X * (venda - k * nota)
            st:     X1 + X3 + ... + Xn = gasto_mwh  (Gasto Total)
                    Xi / gasto_mwh <= 0.75          (Proporção Máxima Unitária)
        
        """
        
        df_geradoras = Utils.global_state["precos_leilao"].merge(
            Utils.global_state["info_geradoras"]
        )[["SiglaVendedor", "PrecoVenda", "NotaSustentabilidade", "Fonte"]]

        quant_geradoras = len(df_geradoras)
        venda = df_geradoras["PrecoVenda"].values
        nota = df_geradoras["NotaSustentabilidade"].values
        gasto_mwh = self.gasto_kwh/1000
        k = venda.mean() / nota.mean() * self.k_sustentabilidade

        X = cp.Variable((quant_geradoras,1))  # nossas variaveis de otimizacao

        objective = cp.Minimize(cp.sum(cp.multiply(X, [venda - k * nota])))
        total_mwh = cp.sum(X) == gasto_mwh
        proporcao = X/gasto_mwh <= 0.75
        constraints = [X >= 0, total_mwh, proporcao]

        problem = cp.Problem(objective, constraints)
        result = problem.solve()
        df_geradoras["Proposta"] = X.value
        df_geradoras_top2 = df_geradoras.sort_values("Proposta", ascending=False)[:2]

        # Informações para o Card
        # O custo da energia é real, mas os demais são estimados conforme proporções pesquisadas
        self.custo_energia = (df_geradoras_top2["Proposta"] * df_geradoras_top2["PrecoVenda"]).sum() * 1.1    # com ajuste de diferenca de data
        self.custo_distribuicao = self.custo_energia * 0.16 / 0.32
        self.custo_transmissao = self.custo_energia * 0.08 / 0.32
        self.encargos = self.custo_energia * 0.23 / 0.32
        self.outros = self.custo_energia * 0.25 / 0.32
        custo = self.custo_energia + self.custo_distribuicao + self.custo_transmissao + self.encargos + self.outros
        self.impostos = custo * (0.40)
        self.custo_final = custo + self.impostos        
        self.contratando = {
            df_geradoras_top2["SiglaVendedor"].iloc[0]:  df_geradoras_top2["Fonte"].iloc[0],
            df_geradoras_top2["SiglaVendedor"].iloc[1]:  df_geradoras_top2["Fonte"].iloc[1]
        }

    def show_card(self, titulo, cor):
        st.markdown(f"""
            <p style='color: {cor}; font-size: 20px; text-align: center'>
            <b>{titulo}</b>
            </p>""", 
            unsafe_allow_html=True
        )
        st.markdown(f"""
            <p style='color: {cor}; font-size: 40px; text-align: center'>
            <b>R$ {int(self.custo_final)}/mês</b>
            </p>""", 
            unsafe_allow_html=True
        )

        st.markdown(f"<p style='color: {cor}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)

        st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>Geração:</b> R$ {round(self.custo_energia,2)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>Distribuição:</b> R$ {round(self.custo_distribuicao,2)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>Transmissão:</b> R$ {round(self.custo_transmissao,2)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>Encargos:</b> R$ {round(self.encargos,2)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>Impostos:</b> R$ {round(self.impostos,2)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>Outros:</b> R$ {round(self.outros,2)}</p>", unsafe_allow_html=True)

        st.markdown(f"<p style='color: {cor}; font-size: 26px;'><b>Contratando:</b></p>", unsafe_allow_html=True)

        for comp in self.contratando.keys():
            empresa = comp
            fonte = self.contratando[empresa]
            st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>{empresa} - {fonte}</b></p>", unsafe_allow_html=True)


class CurrentOption():
    def __init__(self, gasto_kwh):
        self.gasto_kwh = gasto_kwh

    def current_option(self):
        df_distribuidoras = Utils.global_state["tarifas_distribuidoras"][
            ["SigAgente", "VlrTUSD", "VlrTE"]
        ]

        distribuidora_atual = df_distribuidoras[
            df_distribuidoras["SigAgente"] == Utils.global_state["distribuidora"]
        ]

        gasto_mwh = self.gasto_kwh/1000

        # Informação para o Card
        self.tarifa_energia = (distribuidora_atual["VlrTE"] * gasto_mwh).iloc[0]
        self.tarifa_sistema = (distribuidora_atual["VlrTUSD"] * gasto_mwh).iloc[0] 
        custo = self.tarifa_energia + self.tarifa_sistema
        self.impostos = custo * (0.18 + 0.0055 + 0.0255)        # ICMS + PIS/PASEP + COFINS
        self.custo_final = custo + self.impostos
        self.contratando = {
            Utils.global_state["distribuidora"]:  "Distribuidora"
        }

    def show_card(self, titulo, cor):
        st.markdown(f"""
            <p style='color: {cor}; font-size: 20px; text-align: center'>
            <b>{titulo}</b>
            </p>""", 
            unsafe_allow_html=True
        )
        st.markdown(f"""
            <p style='color: {cor}; font-size: 40px; text-align: center'>
            <b>R$ {int(self.custo_final)}/mês</b>
            </p>""", 
            unsafe_allow_html=True
        )

        st.markdown(f"<p style='color: {cor}; font-size: 26px;'><b>Composição:</b></p>", unsafe_allow_html=True)

        st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>Tarifa de Energia:</b> R$ {round(self.tarifa_energia,2)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>Tarifa de Uso do Sistema de Distribuição:</b> R$ {round(self.tarifa_sistema,2)}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>Impostos:</b> R$ {round(self.impostos,2)}</p>", unsafe_allow_html=True)

        st.markdown(f"<p style='color: {cor}; font-size: 26px;'><b>Contratando:</b></p>", unsafe_allow_html=True)

        for comp in self.contratando.keys():
            empresa = comp
            fonte = self.contratando[empresa]
            st.markdown(f"<p style='color: {cor}; font-size: 16px;'><b>{empresa} - {fonte}</b></p>", unsafe_allow_html=True)