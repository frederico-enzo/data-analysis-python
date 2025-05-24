import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
file_path = 'data/world_data.csv'
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

# Filtrar os seis principais continentes
main_continents = ['Africa', 'America', 'Asia', 'Europe', 'Oceania', 'Antarctica']
filtered_data = data[data['continente'].isin(main_continents)]

# Ajustar estilo do gráfico para simplicidade e clareza
sns.set(style="whitegrid", palette="pastel")

# Criar gráfico com facetas por continente
plt.figure(figsize=(15, 8))
g = sns.FacetGrid(filtered_data, col='continente', col_wrap=3, height=4, sharex=False, sharey=False)

# Plotar histogramas com KDE
g.map(sns.histplot, 'crescimento_populacao', kde=True, color='steelblue', bins=15)

# Adicionar média em cada faceta e narrativas
for ax, (continent, data_subset) in zip(g.axes.flat, filtered_data.groupby('continente')):
    mean_value = data_subset['crescimento_populacao'].mean()
    ax.axvline(mean_value, color='crimson', linestyle='--', linewidth=1.5)
    ax.text(mean_value + 0.2, ax.get_ylim()[1] * 0.9, f'{mean_value:.2f}%', 
            color='crimson', fontsize=10, fontweight='bold')

# Ajustar títulos, rótulos e grade
g.set_axis_labels('Crescimento da População (%)', 'Frequência')
g.set_titles('{col_name}', fontsize=12, fontweight='bold')
g.fig.suptitle('Distribuição do Crescimento da População por Continente', fontsize=16, y=1.03, fontweight='bold')

# Melhorar o layout e salvar
plt.subplots_adjust(hspace=0.4, top=0.92)
plt.savefig(os.path.join(output_dir, "crescimento_populacao_gestalt.png"), dpi=300)

# Exibir o gráfico
plt.show()
