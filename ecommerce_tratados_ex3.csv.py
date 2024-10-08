import pandas as pd

# Carregar o DataFrame
df = pd.read_csv('/data/ecommerce_tratados_ex3.csv')

# Criar o campo Qtd_Vendidos_Cod
transformacoes = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+1000': 1000,
    '+10mil': 10000,
    '+50mil': 50000
}

df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(transformacoes)

# Criar o campo Marca_Freq como proporção
frequencias_marca = df['Marca'].value_counts()
df['Marca_Freq'] = df['Marca'].map(frequencias_marca) / len(df)

# Criar o campo Material_Freq
frequencias_material = df['Material'].value_counts()
df['Material_Freq'] = df['Material'].map(frequencias_material) / len(df)

# Visualizar o DataFrame resultante (opcional)
print(df.head())