# import pandas as pd
from pandas import read_csv

# Kaggle - base de dados para estudos!
# https://kaggle.com

# df = DataFrame
df = read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# head() - busca os primeiros 5 dados - head(n) retorna n dados
# info() - retorna os dados principais da base (colunas, tipos, quantidade)
# describe() - retorna dados de análise
# describe(include|exclude) traz mais ou menos dados de análise

print(df.head())
print(df.info())
print(df.describe())
print(df.shape) # tupla (rows, cols)
rows, cols = df.shape # já associa posição = váriavel

# dict - 'chave': 'valor'
colunas_ptbr = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

# rename - troca o nome de algum campo (coluna, index etc)
df.rename(columns=colunas_ptbr, inplace=True)
print(df.head()) 
# df.columns só para as colunas

# value_counts() - contabiliza cada valor de uma determinada coluna
print(df["senioridade"].value_counts())

senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}

# replace() - troca valor por novo valor (ex. 1: sim, 0: não)
df['senioridade'] = df['senioridade'].replace(senioridade)
print(df["senioridade"].value_counts())

# print(df.describe())
print(df.describe(include='all')) # None, all ou dtypes