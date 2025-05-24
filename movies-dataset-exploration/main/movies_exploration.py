import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset fornecido pelo usuário
file_path = 'data\movie_metadata.csv'
movies_df = pd.read_csv(file_path)

# Mostrar as primeiras linhas do dataset e informações básicas
movies_df.head(), movies_df.info()
# Estatísticas descritivas para as colunas de orçamento e bilheteira
budget_gross_stats = movies_df[['budget', 'gross']].describe()

# Remover dados nulos para análise de correlação e visualização
budget_gross_data = movies_df[['budget', 'gross']].dropna()

# Calcular a correlação entre orçamento e bilheteira
correlation = budget_gross_data.corr().loc['budget', 'gross']

# Configurar visualizações
plt.figure(figsize=(14, 6))

# Histograma para Orçamento
plt.subplot(1, 2, 1)
sns.histplot(movies_df['budget'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribuição de Orçamento')
plt.xlabel('Orçamento')
plt.ylabel('Frequência')

# Histograma para Bilheteira
plt.subplot(1, 2, 2)
sns.histplot(movies_df['gross'].dropna(), bins=30, kde=True, color='green')
plt.title('Distribuição de Bilheteira')
plt.xlabel('Bilheteira')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()

# Gráfico de dispersão entre Orçamento e Bilheteira
plt.figure(figsize=(10, 6))
sns.scatterplot(x='budget', y='gross', data=budget_gross_data, alpha=0.5)
plt.title('Relação entre Orçamento e Bilheteira')
plt.xlabel('Orçamento')
plt.ylabel('Bilheteira')
plt.show()

# Exibir estatísticas descritivas e correlação
budget_gross_stats, correlation

# Calcular medidas estatísticas para orçamento e bilheteira
def calculate_statistics(column):
    column_cleaned = column.dropna()  # Remover valores nulos
    mean = column_cleaned.mean()  # Média
    median = column_cleaned.median()  # Mediana
    mode = column_cleaned.mode().iloc[0] if not column_cleaned.mode().empty else None  # Moda
    std_dev = column_cleaned.std()  # Desvio padrão
    amplitude = column_cleaned.max() - column_cleaned.min()  # Amplitude
    return {
        "Média": mean,
        "Mediana": median,
        "Moda": mode,
        "Desvio Padrão": std_dev,
        "Amplitude": amplitude,
    }

# Calcular para orçamento e bilheteira
budget_stats = calculate_statistics(movies_df['budget'])
gross_stats = calculate_statistics(movies_df['gross'])

budget_stats, gross_stats

# Exibir os resultados
print("Estatísticas para Orçamento:")
print(budget_stats)

print("\nEstatísticas para Bilheteira:")
print(gross_stats)

# Configurar visualizações de boxplot
plt.figure(figsize=(14, 6))

# Boxplot para orçamento
plt.subplot(1, 2, 1)
sns.boxplot(data=movies_df, y='budget', color='skyblue')
plt.title('Boxplot de Orçamento')
plt.ylabel('Orçamento')

# Boxplot para bilheteira
plt.subplot(1, 2, 2)
sns.boxplot(data=movies_df, y='gross', color='lightgreen')
plt.title('Boxplot de Bilheteira')
plt.ylabel('Bilheteira')

plt.tight_layout()
plt.show()

# Identificar valores extremos (outliers)
Q1_budget = movies_df['budget'].quantile(0.25)
Q3_budget = movies_df['budget'].quantile(0.75)
IQR_budget = Q3_budget - Q1_budget
outliers_budget = movies_df[movies_df['budget'] > (Q3_budget + 1.5 * IQR_budget)]

Q1_gross = movies_df['gross'].quantile(0.25)
Q3_gross = movies_df['gross'].quantile(0.75)
IQR_gross = Q3_gross - Q1_gross
outliers_gross = movies_df[movies_df['gross'] > (Q3_gross + 1.5 * IQR_gross)]

print("Outliers de Orçamento:")
print(outliers_budget[['movie_title', 'budget']])

print("\nOutliers de Bilheteira:")
print(outliers_gross[['movie_title', 'gross']])