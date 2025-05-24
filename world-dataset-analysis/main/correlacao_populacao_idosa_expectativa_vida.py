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

# Filtrar dados apenas do Brasil
brazil_data = data[data['pais'] == 'Brazil']

# Selecionar as colunas relevantes
selected_columns = ['ano', 'populacao_acima_65', 'expec_vida']
filtered_brazil_data = brazil_data[selected_columns].dropna()

# Verificar se há dados suficientes
if filtered_brazil_data.empty:
    print("Não há dados suficientes para criar o gráfico de dispersão para o Brasil.")
else:
    # Criar gráfico de dispersão
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Plotar população acima de 65 anos como dispersão
    ax1.scatter(filtered_brazil_data['ano'], filtered_brazil_data['populacao_acima_65'], 
                color='#1A85FF', label='População Acima de 65 Anos (%)', s=120, alpha=0.85, edgecolors='black')

    # Criar um segundo eixo y para a expectativa de vida
    ax2 = ax1.twinx()
    ax2.plot(filtered_brazil_data['ano'], filtered_brazil_data['expec_vida'], 
             color='#D41159', marker='o', label='Expectativa de Vida (anos)', linewidth=2)

    # Adicionar anotações narrativas
    max_year = filtered_brazil_data['ano'].max()
    max_life_expectancy = filtered_brazil_data.loc[filtered_brazil_data['ano'] == max_year, 'expec_vida'].values[0]
    ax2.annotate(f"Expectativa de vida em {max_year}: {max_life_expectancy:.1f} anos",
                 xy=(max_year, max_life_expectancy), xytext=(max_year - 5, max_life_expectancy + 2),
                 arrowprops=dict(facecolor='#D41159', arrowstyle='->'),
                 fontsize=12, color='#D41159')

    # Configuração de eixos
    ax1.set_xlabel('Ano', fontsize=14, weight='bold', color='#333333')
    ax1.set_ylabel('População Acima de 65 Anos (%)', fontsize=14, color='#1A85FF', weight='bold')
    ax2.set_ylabel('Expectativa de Vida (anos)', fontsize=14, color='#D41159', weight='bold')

    # Ajustar estilo das legendas
    ax1.legend(loc='upper left', bbox_to_anchor=(0, 1.15), fontsize=12, frameon=False)
    ax2.legend(loc='upper right', bbox_to_anchor=(1, 1.15), fontsize=12, frameon=False)

    # Melhorar a grade para clareza
    ax1.grid(visible=True, linestyle='--', alpha=0.5, color='#CCCCCC')

    # Adicionar título
    plt.title('Relação Entre População Idosa e Expectativa de Vida no Brasil', fontsize=16, weight='bold', color='#333333')

    # Ajustar layout para evitar sobreposição
    plt.tight_layout()

    # Salvar o gráfico em arquivo
    plt.savefig(os.path.join(output_dir, "gestalt_populacao_idosa_expectativa_vida.png"), dpi=300)

    # Exibir o gráfico
    plt.show()
