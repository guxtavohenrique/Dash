import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

df = pd.read_csv("")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)


fig_idade = px.bar(df, y="Total", color="City", title="Qual a sua faixa etária?")
col1.plotly_chart(fig_idade)

fig_sexo = px.bar(df, y="Total", color="City", title="Qual a sua orientação sexual?")
col2.plotly_chart(fig_sexo)

fig_incomodo = px.bar(df, y="Total", color="City", title="Você sente algum incômodo nos dentes ou na boca em geral?")
col3.plotly_chart(fig_incomodo)

fig_spray = px.bar(df, y="Total", color="City", title="Você utiliza spray bucal?")
col4.plotly_chart(fig_spray)

fig_fio = px.bar(df, y="Total", color="City", title="Você utiliza fio dental?")
col5.plotly_chart(fig_fio)

fig_escova = px.bar(df, y="Total", color="City", title="Quantas vezes você escova os dentes por dia?")
col6.plotly_chart(fig_escova)

fig_tratamento = px.bar(df, y="Total", color="City", title="Faz algum tipo de tratamento bucal? (Estético ou corretivo)")
col7.plotly_chart(fig_tratamento)

fig_satisfacao = px.bar(df, y="Total", color="City", title="O quão satisfeito você é em relação a sua saúde bucal?")
col7.plotly_chart(fig_satisfacao)

