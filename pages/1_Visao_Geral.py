
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/avanco_ia_empresas.csv")

st.header("Visão Geral dos Investimentos em IA")

ano = st.sidebar.selectbox("Selecione o ano", sorted(df["ano"].unique(), reverse=True))
df_filtrado = df[df["ano"] == ano]

fig1 = px.bar(df_filtrado.sort_values("investimento_ia_usd_milhoes", ascending=False).head(10),
              x="empresa", y="investimento_ia_usd_milhoes",
              title=f"Top 10 Empresas por Investimento em IA - {ano}",
              color="setor")
st.plotly_chart(fig1, use_container_width=True)
