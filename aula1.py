from pandas import read_csv

# Kaggle - base de dados para devs
# dataframe
df = read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.shape) # tupla (rows, cols)
rows, cols = df.shape # já associa posição = váriavel

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

df.rename(columns=colunas_ptbr, inplace=True)
print(df.head()) # ou df.columns só para as colunas

print(df["senioridade"].value_counts())

senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}

df['senioridade'] = df['senioridade'].replace(senioridade)
print(df["senioridade"].value_counts())

# print(df.describe())
print(df.describe(include='all')) # None, all ou dtypes