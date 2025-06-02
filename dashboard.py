
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título do dashboard
st.title("📊 Dashboard de Maturidade Empresarial - Acelera Gastronomia")

# Carregando os dados (exemplo: substitua pelos seus arquivos reais)
@st.cache_data
def carregar_dados():
    # Supondo que você já tenha os dados processados em CSV ou Excel
    ranking = pd.read_csv("ranking_empresas.csv")
    categorias = pd.read_csv("media_categorias.csv")
    diagnostico = pd.read_csv("diagnostico_detalhado.csv")
    return ranking, categorias, diagnostico

ranking, categorias, diagnostico = carregar_dados()

# Filtro por empresa
empresas = ranking["Empresa Limpa"].unique()
empresa_selecionada = st.selectbox("Selecione uma empresa para análise detalhada:", empresas)

# Mostrar média geral por empresa
st.subheader("Média Geral de Maturidade por Empresa")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x="Média Geral", y="Empresa Limpa", data=ranking.sort_values("Média Geral"), ax=ax1, palette="viridis")
st.pyplot(fig1)

# Comparativo por categoria para a empresa selecionada
st.subheader(f"Radar de Maturidade por Categoria - {empresa_selecionada}")
df_empresa = diagnostico[diagnostico["Empresa Limpa"] == empresa_selecionada]
df_radar = df_empresa.groupby("Categoria")["Nota"].mean().reset_index()

categories = list(df_radar["Categoria"])
values = list(df_radar["Nota"])
values += values[:1]  # Fechar o gráfico

import numpy as np
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig2, ax2 = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax2.plot(angles, values, linewidth=2, linestyle='solid')
ax2.fill(angles, values, alpha=0.25)
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(categories, fontsize=8)
ax2.set_title(f"Radar de {empresa_selecionada}")
st.pyplot(fig2)

# Faixas de Maturidade
st.subheader("Distribuição por Faixa de Maturidade")
faixas = pd.cut(ranking["Média Geral"], bins=[0, 2, 3, 4, 5],
                labels=["🔴 Baixa", "🟡 Média", "🟢 Boa", "🌟 Excelência"])
fig3, ax3 = plt.subplots()
faixas.value_counts().sort_index().plot(kind='barh', ax=ax3, color=["red", "gold", "green", "blue"])
ax3.set_xlabel("Número de Empresas")
ax3.set_ylabel("Faixa")
ax3.set_title("Distribuição das Empresas por Faixa")
st.pyplot(fig3)

# Tabela completa (opcional)
st.subheader("📋 Dados Detalhados do Diagnóstico")
st.dataframe(diagnostico[diagnostico["Empresa Limpa"] == empresa_selecionada])
