
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/avanco_ia_empresas.csv")

st.header("Comparativo de Investimento e Crescimento de Lucro")

empresas = st.multiselect("Selecione as empresas", options=df["empresa"].unique(), default=[df["empresa"].unique()[0]])

df_filtrado = df[df["empresa"].isin(empresas)]

fig = px.scatter(df_filtrado, x="investimento_ia_usd_milhoes", y="crescimento_lucro_%",
                 color="empresa", size="nota_inovacao",
                 hover_data=["ano", "setor"],
                 title="Investimento em IA vs Crescimento de Lucro (%)")
st.plotly_chart(fig, use_container_width=True)
