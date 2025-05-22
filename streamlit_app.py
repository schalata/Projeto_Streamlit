# Importando as bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregando os dados
dados = pd.read_excel('Vendas_Base_de_Dados.xlsx')

# Exibindo informações e gráficos: mostrar o título do painel e exibir a tabela
st.title("Dashboard de Vendas")
st.write("Tabela de vendas do mês:")
st.dataframe(dados)

# Calcula o faturamento em cada linha
dados['Faturamento'] = dados['Quantidade'] * dados['Valor Unitário']

# Agrupa e ordena o faturamento por loja (do maior para o menor)
dados = (
    dados.groupby('Loja')['Faturamento']
    .sum()
    .reset_index()
    .sort_values(by='Faturamento', ascending=False)
)

# st.write(dados)

# Criar um gráfico de barras com o faturamento por loja
grafico = px.bar(dados, x='Loja', y='Faturamento', title='Faturamento por Loja')
st.plotly_chart(grafico)

#  Inserir um filtro para escolher uma loja e ver os dados dela
lojas = sorted(dados['Loja'].unique())
loja_escolhida = st.selectbox('Escolha a loja:', lojas)

dados_loja = dados[dados['Loja'] == loja_escolhida]
st.write(f'Dados da loja {loja_escolhida}:')
st.dataframe(dados_loja)