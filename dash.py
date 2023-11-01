from asyncore import write
from tkinter import CENTER
from turtle import title, width
import streamlit as st
import pandas as pd
import plotly.express as px

#comando para ampliar o banco
st.set_page_config(layout="wide")

#comando para colocar titulo
st.title("Projeto de análise e estratégia de tratamento bucal")

#comando para colocar subtitulo
st.subheader("Introdução", divider='rainbow')

#comando para colocar texto
st.write("O quadro abaixo é um pequeno banco de dados em Excel obtido atráves de uma pesquisa online utilizando o site Google Formulários.")
st.write("As respostas obtidas serviram como uma base sólida de dados para se estudar as rotinas de quem se preocupa com a saúde bucal.")

#comando para colocar subtitulo
st.subheader("Respostas do Formulário", divider='rainbow')

#comando para ler o banco de dados em excell
df = pd.read_excel("respostas.xlsx", engine="openpyxl")
df

#comando para colocar subtitulo
st.header("Infográficos da Pesquisa")

#comando para colocar subtitulo
st.subheader("Informações Pessoais dos Participantes", divider='rainbow')


#dividindo as colunas no streamlit
col1, col2 = st.columns(2)

#comando para criar gráfico para idade
fig_idade = px.bar(df, x="Qual a sua faixa etária?", color="Qual a sua orientação sexual?", title="Faixa Etária dos participantes")
col1.plotly_chart(fig_idade)

#comando para criar gráfico para sexo
fig_sexo = px.bar(df, x="Qual a sua orientação sexual?", color="Qual a sua orientação sexual?", title="Orientação sexual dos participantes")
col2.plotly_chart(fig_sexo)

#comando para colocar subtitulo
st.subheader("Rotina dos Participantes", divider='rainbow')

#dividindo as colunas no streamlit
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)

#comando para criar gráfico para incomodo
fig_incomodo = px.bar(df, x="Você sente algum incômodo nos dentes ou na boca em geral?", color="Qual a sua orientação sexual?", title="Participantes que sentem algum incômodo nos dentes")
col3.plotly_chart(fig_incomodo)

#comando para criar gráfico para quem usa spray bucal
fig_spray_bucal = px.bar(df, y="Você utiliza spray bucal?", color="Qual a sua orientação sexual?", title="Participantes que usam 'Spray Bucal'")
col4.plotly_chart(fig_spray_bucal)

#comando para criar gráfico para quem usa fio dental
fig_fio_dental = px.bar(df, x="Você utiliza fio dental?", color="Qual a sua orientação sexual?", title="Participantes que utilizam 'Fio Dental'")
col5.plotly_chart(fig_fio_dental)

#comando para criar gráfico para quantas vezes escovam os dentes
fig_escova = px.bar(df, x="Quantas vezes você escova os dentes por dia?", color="Qual a sua orientação sexual?", title="Rotina dos participantes na hora de 'Escovar os Dentes'")
col6.plotly_chart(fig_escova)

#comando para criar gráfico para quem faz tratamento bucal
fig_tratamento = px.bar(df, x="Faz algum tipo de tratamento bucal? (Estético ou corretivo)", color="Qual a sua orientação sexual?", title="Quantos participantes fazem tratamento bucal (Estético ou Corretivo)")
col7.plotly_chart(fig_tratamento)

#comando para criar gráfico para quem gostaria de fazer tratamento
fig_tratamento2 = px.bar(df, x="Se sua resposta foi não, você gostaria ou acharia necessário fazer algum tratamento mesmo que seja estético?", color="Qual a sua orientação sexual?", title="Quantos participantes gostaria de fazer algum tratamento bucal (Estético ou Corretivo)")
col8.plotly_chart(fig_tratamento2)

#comando para colocar subtitulo
st.subheader("FeedBack dos Participantes", divider='rainbow')

#dividindo as colunas no streamlit
col9, col10 = st.columns(2)

#comando para criar gráfico para quem acredita na saúde bucal organizada aumenta à autoestima
fig_autoestima = px.bar(df, x="Você acha que ter uma saúde bucal organizada melhora a autoestima?", color="Qual a sua orientação sexual?", title="Participantes que acreditam na autoestima tendo uma saúde bucal organizada")
col9.plotly_chart(fig_autoestima)

#comando para criar gráfico para quem está satisfeito com a saúde bucal
fig_satisfeito = px.bar(df, x="O quão satisfeito você é em relação a sua saúde bucal?", color="Qual a sua orientação sexual?", title="Participantes que estão satisfeito ou não com a sua saúde bucal")
col10.plotly_chart(fig_satisfeito)