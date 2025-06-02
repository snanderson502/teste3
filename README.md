# 📊 Dashboard de Maturidade Empresarial - Acelera Gastronomia

Este projeto apresenta um painel interativo desenvolvido com **Streamlit** para visualização e análise dos diagnósticos de maturidade de micro e pequenas empresas atendidas pelo programa **Acelera Gastronomia**.

## ✅ Funcionalidades

- Média geral de maturidade por empresa
- Radar comparativo por categoria
- Distribuição por faixa de maturidade (baixa, média, boa, excelência)
- Visualização detalhada por empresa
- Tabela interativa com notas e observações

## 📁 Arquivos incluídos

- `dashboard.py`: código principal do dashboard em Streamlit
- `ranking_empresas.csv`: média geral por empresa
- `media_categorias.csv`: média geral por categoria
- `diagnostico_detalhado.csv`: base com todas as respostas dos diagnósticos

## 🚀 Como executar localmente

1. Clone este repositório ou baixe os arquivos
2. Instale as dependências:

```bash
pip install streamlit pandas matplotlib seaborn
```

3. Execute o dashboard:

```bash
streamlit run dashboard.py
```

## 🌐 Publicar no Streamlit Cloud

Você pode publicar este projeto online em https://streamlit.io/cloud conectando seu repositório do GitHub e apontando para o arquivo `dashboard.py`.

---

Desenvolvido para uso em consultorias e apresentações com foco em transformação digital, gestão e inovação para pequenos negócios do setor de alimentação. 🍽️
