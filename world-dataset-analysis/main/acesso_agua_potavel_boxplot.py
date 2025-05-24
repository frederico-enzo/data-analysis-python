import os
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo enviado
file_path = 'data/world_data.csv'

# Carregar os dados
data = pd.read_csv(file_path)

# Criar a pasta "graficos" se não existir
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# Ajustar nomes de continentes para unificar
data['continente'] = data['continente'].replace({
    'North America': 'America',
    'South America': 'America',
    'Australasia': 'Oceania',
    'Central America': 'America',
    'Europe & Central Asia': 'Europe',
    'East Asia & Pacific': 'Asia',
    'Sub-Saharan Africa': 'Africa'
})

# Filtrar os seis principais continentes (incluindo Antártida)
main_continents = ['Africa', 'America', 'Asia', 'Europe', 'Oceania', 'Antarctica']
filtered_data = data[data['continente'].isin(main_continents)]

# Preparar dados para o box-plot: acesso à água potável por continente
boxplot_data = filtered_data[['continente', 'acesso_agua_potavel']].dropna()

# Criar o boxplot ajustado
plt.figure(figsize=(10, 6))
box = boxplot_data.boxplot(
    by='continente',
    column='acesso_agua_potavel',
    grid=False,
    patch_artist=True,
    boxprops=dict(facecolor='#AEDFF7', color='#2A6EBB'),
    medianprops=dict(color='#D72638', linewidth=2),
    whiskerprops=dict(color='#2A6EBB'),
    capprops=dict(color='#2A6EBB'),
    flierprops=dict(markerfacecolor='#FFDD67', markeredgecolor='#FF5733', markersize=8),
    showfliers=False
)

# Ajustar o gráfico para uma estética de storytelling
plt.title("Acesso à Água Potável por Continente", fontsize=16, weight='bold', color='#333333')
plt.suptitle("")  # Remover título automático
plt.xlabel("Continente", fontsize=12, weight='bold', color='#333333')
plt.ylabel("Proporção de Acesso à Água Potável (%)", fontsize=12, weight='bold', color='#333333')
plt.xticks(rotation=45, fontsize=11, weight='bold', color='#333333')
plt.yticks(fontsize=10, color='#333333')

# Adicionar linhas horizontais para referência
plt.grid(axis='y', linestyle='--', alpha=0.6, color='#CCCCCC')

# Adicionar uma anotação narrativa
plt.annotate(
    "Europa possui os maiores índices de acesso.",
    xy=(3, 95), xytext=(2, 85),
    arrowprops=dict(facecolor='#D72638', shrink=0.05, width=2),
    fontsize=11, color='#D72638'
)

# Salvar o gráfico em um arquivo PNG
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "acesso_agua_potavel_boxplot_gestalt.png"), dpi=300)

plt.show()
