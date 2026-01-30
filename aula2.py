from pandas import read_csv, DataFrame
from numpy import nan

df = read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

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

senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}

df.rename(columns=colunas_ptbr, inplace=True)
df['senioridade'] = df['senioridade'].replace(senioridade)

print(df.isnull().sum()) # mostra quantos dados de cada coluna são nulos

print(df['ano'].unique()) # valores presentes nos campos, ignorando as repetições

print(df[df.isnull().any(axis=1)]) # mostra as linhas que possuem dados nulos

df_salarios = DataFrame({
    'nome': ['Ana', 'Bia', 'Carlos', 'Daniel', 'Eva'],
    'salario': [3500, 4200, nan, 5000, nan]
})

# calcula a media e a mediana dos salarios no lugar de valores nulos
df_salarios['salario_media'] = df_salarios['salario'].fillna(round(df_salarios['salario'].mean(), 2))
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(round(df_salarios['salario'].median(), 2))

print(df_salarios)


# fillna(valor) - preenche os valores nulos com um valor
# ffill() - preenche com o valor anterior
# bfill() - preenche com o valor posterior

df_limpo = df.dropna() # remove os dados nulos e copia o df
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int')) # converte o tipo da coluna
