import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho do arquivo enviado
file_path = 'data/world_data.csv'

# Carregar os dados
data = pd.read_csv(file_path)

# Criar a pasta "graficos" se não existir
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# Selecionar os países específicos, com foco no Brasil
selected_countries = ["Brazil", "United States", "India", "China", "Germany"]
line_chart_data = data[data['pais'].isin(selected_countries)][['ano', 'pais', 'populacao_acima_65']].dropna()

# Configurar a paleta de cores e estilo
sns.set(style="whitegrid")
colors = sns.color_palette("Set2", len(selected_countries))

# Criar gráfico de linhas para esses países
plt.figure(figsize=(14, 8))  # Tamanho maior para melhor visualização
for i, country in enumerate(selected_countries):
    country_data = line_chart_data[line_chart_data['pais'] == country]
    
    # Destacar o Brasil
    if country == "Brazil":
        plt.plot(country_data['ano'], country_data['populacao_acima_65'], label=country, 
                 linewidth=3, marker='o', markersize=8, color=colors[i], zorder=5)  # Linha mais grossa e com mais destaque
    else:
        plt.plot(country_data['ano'], country_data['populacao_acima_65'], label=country, 
                 linewidth=2, marker='o', markersize=6, color=colors[i], zorder=4)  # Outras linhas com menos destaque

# Melhorar escala e legibilidade
plt.title("Proporção da População Acima de 65 Anos (Indicador Indireto de Expectativa de Vida)", fontsize=18, fontweight='bold')
plt.xlabel("Ano", fontsize=16)
plt.ylabel("População Acima de 65 Anos (%)", fontsize=16)

# Ajustar o eixo y para uma escala mais adequada
plt.ylim(0, 28)  # Ajustar limite superior

# Ajustar os ticks do eixo Y para 4 em 4
plt.yticks(range(0, 28, 4))  # De 0 até 28, com incremento de 4

# Ajustar a exibição do eixo X para todos os anos
plt.xticks(ticks=sorted(line_chart_data['ano'].unique()), rotation=45, fontsize=14)

# Adicionar legenda e ajustar posição
plt.legend(title="Países", fontsize=14, title_fontsize=16, loc='upper left', bbox_to_anchor=(1, 1), borderpad=1)

# Melhorar a grade do gráfico com mais visibilidade
plt.grid(visible=True, linestyle='--', alpha=0.7, linewidth=1.0)

# Focar no Brasil: Adicionar uma anotação para um evento relevante
brazil_data = line_chart_data[line_chart_data['pais'] == "Brazil"]
max_year = brazil_data.loc[brazil_data['populacao_acima_65'].idxmax()]
min_year = brazil_data.loc[brazil_data['populacao_acima_65'].idxmin()]

# Anotações para maior destaque
plt.annotate(f"Máximo: {max_year['ano']} ({max_year['populacao_acima_65']}%)", 
             xy=(max_year['ano'], max_year['populacao_acima_65']), xycoords='data',
             xytext=(10, 10), textcoords='offset points', arrowprops=dict(arrowstyle="->", lw=1.5),
             fontsize=14, color='red', weight='bold')

plt.annotate(f"Mínimo: {min_year['ano']} ({min_year['populacao_acima_65']}%)", 
             xy=(min_year['ano'], min_year['populacao_acima_65']), xycoords='data',
             xytext=(-15, -15), textcoords='offset points', arrowprops=dict(arrowstyle="->", lw=1.5),
             fontsize=14, color='red', weight='bold')

# Ajustar layout para melhor visibilidade
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "expectativa_vida_brasil_foco_aprimorado.png"))

# Exibir gráfico
plt.show()
