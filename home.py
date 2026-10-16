import pandas as pd
import streamlit as st
import joblib
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Machine Learning', layout='wide')

st.header('Machine Learning - Previsão de Lucro do E-Commerce', text_alignment='center')

st.subheader('Selecione as opções abaixo:')

@st.cache_resource
def load_data():
    load_dotenv()
    conn = create_engine(
        os.getenv('DATABASE_URL')
    )

    query = 'SELECT * FROM sales_analytics.sales_customer_analytics'

    df = pd.read_sql(sql=query, con=conn)
    return df

net_sales = st.number_input(
    label='Vendas Líquidas',
    min_value=100,
    max_value=17_000,
    step=100
)

tax_amount = st.number_input(
    label='Valor do Imposto',
    min_value=0,
    max_value=2_000,
    step=50
)

gross_sales = st.number_input(
    label='Vendas Brutas',
    min_value=100,
    max_value=16_000,
    step=100
)

profit_margin_percentage = st.number_input(
    label='Percentual da Margem de Lucro',
    min_value=0,
    max_value=75,
    step=5
)

product_cost = st.slider(
    label='Custo do Produto',
    min_value=2,
    max_value=9_000,
    step=100
)


loyalty_points_earned = st.slider(
    label='Pontos de Lealdade Conquistados',
    min_value=0,
    max_value=1_600,
    step=5
)

discount_amount = st.slider(
    label='Valor do Desconto',
    min_value=0,
    max_value=6_700,
    step=10
)

quantity = st.slider(
    label='Quantidade',
    min_value=0,
    max_value=1_600,
    step=5
)

sales_channel = st.selectbox(
    label='Canal de Vendas',
    options=['Mobile App', 'Social Media', 'Website', 'Marketplace']
)

marketing_channel = st.selectbox(
    label='Canal de Marketing',
    options=[ 'Organic Search',       'Instagram',      'Google Ads', 'Email Marketing',
          'Direct',    'Facebook Ads',        'Referral',       'Affiliate',
          'TikTok',         'YouTube']
)

if st.button(label='⏳Rodar Previsão 👈 clique aqui', use_container_width=True):
    df = pd.DataFrame({
        'net_sales': [net_sales], 
        'tax_amount': [tax_amount], 
        'gross_sales': [gross_sales], 
        'profit_margin_percentage': [profit_margin_percentage],
        'product_cost': [product_cost], 
        'loyalty_points_earned': [loyalty_points_earned], 
        'discount_amount': [discount_amount], 
        'quantity': [quantity], 
        'sales_channel': [sales_channel], 
        'marketing_channel': [marketing_channel]
    })

    modelo = joblib.load('modelo/modelo.joblib')

    df['profit'] = modelo.predict(df)

    
    st.markdown(f"""
    <h3>Resumo da venda</h3>

    <h5 style="font-weight: normal;">
        A venda foi realizada pelo canal
        <strong>{df['sales_channel'].iloc[0]}</strong>,
        com origem em <strong>{df['marketing_channel'].iloc[0]}</strong>.
    </h5>

    <h5 style="font-weight: normal;">
        O valor das vendas foi de
        <strong>R$ {df['gross_sales'].iloc[0]:.2f}</strong>,
        com <strong>R$ {df['tax_amount'].iloc[0]:.2f}</strong>
        em impostos e
        <strong>R$ {df['discount_amount'].iloc[0]:.2f}</strong>
        em descontos.
    </h5>

    <h5 style="font-weight: normal;">
        O custo do produto foi de
        <strong>R$ {df['product_cost'].iloc[0]:.2f}</strong>,
        com margem de lucro de
        <strong>{df['profit_margin_percentage'].iloc[0]}%</strong>.
    </h5>

    <h5 style="font-weight: normal;">
        Foram registradas <strong>{df['quantity'].iloc[0]}</strong>
        unidades vendidas e
        <strong>{df['loyalty_points_earned'].iloc[0]}</strong>
        pontos de fidelidade.
    </h5>

    <h5 style="font-weight: normal;">
        O valor registrado foi de
        <strong>R$ {df['profit'].iloc[0]:.2f}</strong>,
        representando o resultado financeiro da venda.
    </h5>

    <h5 style="font-weight: normal;">
        A técnica estatística de Machine Learning utilizada para prever os resultados
        foi a Regressão Linear.
    </h5>
    """, unsafe_allow_html=True)

st.header('Análise Estatística Descritiva', text_alignment='center')

df = load_data()

col1, col2 = st.columns(2)

df = df[df['gender'] != 'Non-Binary']

with col1:
    # GRÁFICO DE GÊNERO
    fig = px.pie(
        data_frame=df,
        names='gender',
        title='Gráfico de Gênero'
    )

    fig.update_layout(title_x=0.3, title_font_size=24)

    st.plotly_chart(fig)


    # GRÁFICO DE CANAL DE VENDAS
    aux = df.groupby(['sales_channel', 'gender']).size().reset_index(name='count')
    aux = aux.sort_values(by='count', ascending=False)

    fig = px.funnel(
        data_frame=aux,
        x='count',
        y='sales_channel',
        color='gender',
        title='Gráfico de Funil de Vendas por Gênero',
        labels={'sales_channel': 'Canal de Vendas', 'count': 'Quantidade', 'gender': 'Gênero'}
    )

    fig.update_layout(title_x=0.1, title_font_size=24)

    st.plotly_chart(fig)

with col2:
    # GRÁFICO DE FAIXA ETARIA
    bins = [18, 25, 35, 45, 55, 74]
    labels = ['18-25', '26-35', '36-45', '46-55', '70+']

    age_group = pd.cut(
        x=df['customer_age'],
        bins=bins,
        labels=labels,
    )

    df['age_group'] = age_group

    group = (
        df.groupby(['age_group', 'gender'], observed=True)
        .agg(
            count=('customer_age', 'count')
        )
        .reset_index()
    )

    fig = px.bar(
        data_frame=group,
        x='age_group',
        y='count',
        color='gender',
        barmode='group',
        title='Gráfico de Faixa Etária por Gênero',
        labels={'age_group': 'Faixas', 'count': 'Quantidade', 'gender': 'Gênero'}
    )

    fig.update_layout(title_x=0.1, title_font_size=24)

    st.plotly_chart(fig)

    aux = (df[['gender', 'marketing_channel']]
           .groupby(['gender', 'marketing_channel'])
           .agg(
               count=('marketing_channel', 'count')
           )
           .reset_index()
           )

    aux = aux.sort_values(by='count')

    fig = px.bar(
        data_frame=aux,
        x='count',
        y='marketing_channel',
        color='gender',
        title='Gráfico de Canal de Marketing por Gênero',
        barmode='group',
        labels={'marketing_channel': 'Canal de Marketing', 'gender': 'Gênero', 'count': 'Quantidade'}
    )

    fig.update_layout(title_x=0.1, title_font_size=24)

    st.plotly_chart(fig)

    

