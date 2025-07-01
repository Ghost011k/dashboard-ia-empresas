
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/avanco_ia_empresas.csv")

st.header("Análise por Setor")

setores = df["setor"].unique()
setor = st.selectbox("Selecione o setor", setores)

df_setor = df[df["setor"] == setor]

fig1 = px.line(df_setor.groupby("ano").investimento_ia_usd_milhoes.mean().reset_index(),
               x="ano", y="investimento_ia_usd_milhoes",
               title=f"Evolução Média do Investimento em IA no Setor {setor}")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(df_setor.groupby("empresa").nota_inovacao.mean().reset_index().sort_values("nota_inovacao", ascending=False),
              x="empresa", y="nota_inovacao",
              title=f"Média da Nota de Inovação no Setor {setor}")
st.plotly_chart(fig2, use_container_width=True)
