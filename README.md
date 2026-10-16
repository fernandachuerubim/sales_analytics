# Sales Analytics

Projeto de análise de vendas de e-commerce com previsão de lucro utilizando Machine Learning (Regressão Linear) e dashboards estatísticos construídos com Streamlit pelo link https://fc-salesanalytics.streamlit.app/.

## 📋 Sobre o projeto

O **Sales Analytics** é uma aplicação Streamlit que permite:

- **Prever o lucro de vendas** de e-commerce com base em características da venda (canal de vendas, canal de marketing, valores brutos/liquidos, impostos, descontos, custo do produto, margem de lucro, quantidade, pontos de fidelidade), utilizando um modelo de Regressão Linear treinado.
- **Visualizar análises estatísticas descritivas** dos dados de vendas, incluindo distribuição por gênero, funil de vendas por canal, faixa etária e canais de marketing.

## 🗂️ Estrutura do repositório

```
sales_analytics/
├── home.py                 # Aplicação Streamlit principal
├── notebook/
│   └── dados.ipynb         # Notebook de exploração e análise de dados
├── modelo/
│   └── modelo.joblib       # Modelo de Machine Learning treinado (Regressão Linear)
├── dataset/
│   ├── ecommerce_sales_customer_analytics_150k.csv  # Base principal de vendas (150k registros)
│   ├── customer_master.csv
│   ├── product_catalog.csv
│   ├── order_items.csv
│   ├── arquivo_pronto.csv
│   └── dataset_statistics.csv
├── pyproject.toml          # Configuração e dependências do projeto (uv)
├── uv.lock                 # Lockfile do uv
├── .python-version         # Versão do Python (3.14)
├── .env                    # Variáveis de ambiente (não versionado)
├── .gitignore
└── README.md
```

## 🚀 Como executar

### Pré-requisitos

- Python >= 3.14
- [uv](https://github.com/astral-sh/uv) (gerenciador de pacotes utilizado pelo projeto)

### Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/fernandachuerubim/sales_analytics.git
cd sales_analytics
uv sync
```

### Configuração de ambiente

Crie um arquivo `.env` na raiz do projeto com a variável de conexão ao banco de dados:

```env
DATABASE_URL=postgresql+psycopg2://usuario:senha@host:porta/banco
```

O app lê a tabela `sales_analytics.sales_customer_analytics` através do SQLAlchemy.

### Executar a aplicação

```bash
uv run streamlit run home.py
```

## 📊 Funcionalidades

### 1. Previsão de Lucro (Machine Learning)

Formulário para prever o lucro de uma venda informando:

- Vendas Líquidas
- Valor do Imposto
- Vendas Brutas
- Percentual da Margem de Lucro
- Custo do Produto
- Pontos de Fidelidade
- Valor do Desconto
- Quantidade
- Canal de Vendas (Mobile App, Social Media, Website, Marketplace)
- Canal de Marketing (Organic Search, Instagram, Google Ads, Email Marketing, Direct, Facebook Ads, Referral, Affiliate, TikTok, YouTube)

O modelo retorna o valor previsto de lucro da venda, exibindo também um resumo da transação.

### 2. Análise Estatística Descritiva

Gráficos interativos gerados com Plotly:

- Gráfico de pizza de gênero
- Funil de vendas por canal e gênero
- Faixa etária por gênero
- Canal de marketing por gênero

## 🛠️ Tecnologias

- [Streamlit](https://streamlit.io/) — interface web
- [pandas](https://pandas.pydata.org/) — manipulação de dados
- [Plotly](https://plotly.com/) — visualizações interativas
- [scikit-learn](https://scikit-learn.org/) — Machine Learning (Regressão Linear)
- [joblib](https://joblib.readthedocs.io/) — serialização do modelo
- [SQLAlchemy](https://www.sqlalchemy.org/) + [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) — conexão ao PostgreSQL
- [python-dotenv](https://pypi.org/project/python-dotenv/) — variáveis de ambiente
- [uv](https://github.com/astral-sh/uv) — gerenciamento de dependências

## 📁 Dataset

O dataset principal contém 150.000 registros de vendas de e-commerce com informações de pedidos, clientes, pagamentos, produtos, marketing e lucro.

## 📋 Link do Kaggle

https://www.kaggle.com/datasets/datascikhan/e-commerce-sales-and-customer-analytics



