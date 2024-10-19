import streamlit as st
import pandas as pd
import plotly.express as plx

st.write(""" Escolha um arquivo CSV com os dados do candidato""")

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=';', encoding='latin1')
    st.dataframe(df, width=1000, height=300)

    df_group_by_education = df.groupby('DS_GRAU_INSTRUCAO').size().reset_index(name='Quantidade')
    fig = plx.bar(df_group_by_education, x='DS_GRAU_INSTRUCAO', y='Quantidade', title='Distribuição por Grau de instrução')
    st.plotly_chart(fig)


    df_group_by_education_and_gender = df.groupby(['DS_GRAU_INSTRUCAO', 'DS_GENERO']).size().reset_index(name='Quantidade')
    print(df_group_by_education_and_gender)
    fig_2 = plx.bar(df_group_by_education_and_gender, x='DS_GRAU_INSTRUCAO', color="DS_GENERO", y='Quantidade', title='Relação entre Grau de instrução e Gênero', barmode='group') 
    st.plotly_chart(fig_2)

    df_group_by_race = df.groupby('DS_COR_RACA').size().reset_index(name='Quantidade')
    fig_3 = plx.pie(df_group_by_race, names='DS_COR_RACA', values='Quantidade', title='Distribuição da cor/raça dos candidatos')
    st.plotly_chart(fig_3)

    df_group_by_gender = df.groupby('DS_GENERO').size().reset_index(name='Quantidade')
    fig_4 = plx.pie(df_group_by_gender, names='DS_GENERO', values='Quantidade', title='Distribuição do gênero dos candidatos')
    st.plotly_chart(fig_4)

    df_female_candidates = df[df['DS_GENERO'] == 'FEMININO']
    df_group_by_party_and_gender = df_female_candidates.groupby('SG_PARTIDO').size().reset_index(name='Quantidade').sort_values(by='Quantidade', ascending=False)
    fig_5 = plx.bar(df_group_by_party_and_gender, x='SG_PARTIDO', y='Quantidade', title='Proporção de candidatas femininas por partido')
    st.plotly_chart(fig_5)

    df_ma_candidates = df[df['DS_GENERO'] == 'MASCULINO']
    df_group_by_party_and_gender_2 = df_ma_candidates.groupby('SG_PARTIDO').size().reset_index(name='Quantidade').sort_values(by='Quantidade', ascending=False)
    fig_6 = plx.bar(df_group_by_party_and_gender_2, x='SG_PARTIDO', y='Quantidade', title='Proporção de candidatos masculinos por partido')
    st.plotly_chart(fig_6)


    
