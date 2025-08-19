# -*- coding: utf-8 -*-
"""
Script para limpeza e preparação inicial do dataset de comportamento de clientes de e-commerce.
"""

# 1. Importar a biblioteca Pandas
import pandas as pd
import numpy as np # Import numpy for NaN values

# --- CONFIGURAÇÃO ---
file_path = 'customer.csv'

# 2. Carregar o Dataset
try:
    # O separador padrão ',' é o correto para a leitura deste arquivo.
    df = pd.read_csv(file_path, sep=',')
    print("Arquivo CSV carregado com sucesso!\n")
except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    print("Por favor, verifique se o nome do arquivo está correto e considere usar o caminho absoluto (completo) do arquivo.")


# 3. Limpeza e Formatação das Colunas
print("--- 3. Renomeando Colunas ---")
print("Nomes das colunas originais:")
print(df.columns)

# Renomeia todas as colunas para o padrão "snake_case" (minúsculas e com underscores)
df.columns = df.columns.str.replace(' ', '_').str.lower()

print("\nNomes das colunas formatados:")
print(df.columns)
print("\n")


# 4. Conversão de Tipos de Dados (Lidando com Formato Numérico Brasileiro/Europeu)
print("--- 4. Corrigindo Tipos de Dados Numéricos ---")

# Lista de colunas que podem estar como texto devido à formatação com vírgula
numeric_cols_to_clean = ['total_spend', 'average_rating']

for col in numeric_cols_to_clean:
    if col in df.columns and df[col].dtype == 'object':
        print(f"Processando a coluna '{col}'...")
        # Garante que a coluna é do tipo string para usar os métodos .str
        df[col] = df[col].astype(str)
        # Passo A: Remover o ponto de milhar (ex: '1.500,50' -> '1500,50')
        df[col] = df[col].str.replace('.', '', regex=False)
        # Passo B: Substituir a vírgula de decimal por um ponto (ex: '1500,50' -> '1500.50')
        df[col] = df[col].str.replace(',', '.', regex=False)
        # Passo C: Converter a coluna para o tipo numérico (float)
        df[col] = pd.to_numeric(df[col], errors='coerce')

print("\nTipos de dados após a conversão:")
df.info()
print("\n")


# 5. Tratamento de Valores Ausentes Específicos
print("--- 5. Tratando Valores Ausentes Específicos ---")
# Preenche os valores em branco na coluna 'satisfaction_level' para clientes específicos.
df.loc[df['customer_id'].isin([172, 244]), 'satisfaction_level'] = 'Neutral'

# Remove espaços em branco de outras entradas na coluna, caso existam
if 'satisfaction_level' in df.columns:
    df['satisfaction_level'] = df['satisfaction_level'].str.strip()
    # Preenche qualquer valor que ficou vazio após o strip
    df['satisfaction_level'].replace('', np.nan, inplace=True)

print("Valores de 'satisfaction_level' para os clientes 172 e 244 foram preenchidos.\n")


# 6. Verificação Geral de Valores Ausentes
print("--- 6. Verificação Geral de Valores Ausentes ---")
missing_values = df.isnull().sum()
print(missing_values)
print("\n")

if missing_values.sum() == 0:
    print("Ótima notícia! Não há mais valores ausentes no dataset.")
else:
    print("Atenção: Ainda existem valores ausentes. Pode ser necessário um tratamento adicional.")

# 7. Exibindo as primeiras linhas do DataFrame limpo
print("\n--- Amostra dos Dados Limpos (Primeiras 5 Linhas) ---")
print(df.head())


# 8. Exportar o DataFrame Limpo para Power BI (Formato Brasileiro/Europeu)
# Salva o DataFrame final em um novo arquivo CSV, formatado para ser lido corretamente por Power BI em regiões que usam vírgula como decimal.
# sep=';' -> Usa ponto e vírgula como separador de colunas para evitar conflito com a vírgula do decimal.
# decimal=',' -> Usa a vírgula como separador decimal (ex: 1120,2).
# index=False -> Evita que o Pandas escreva o índice do DataFrame como uma coluna no arquivo.
output_filename = 'customer_limpo.csv'
df.to_csv(output_filename, index=False, sep=';', decimal=',')

print(f"\n--- Exportação Concluída ---")
print(f"O DataFrame limpo foi salvo com sucesso no arquivo: '{output_filename}'")
print("O arquivo foi formatado com ';' como separador de colunas e ',' como separador decimal.")
