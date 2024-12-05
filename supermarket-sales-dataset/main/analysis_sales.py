import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_csv('supermarket-sales-dataset\data\sales-dataset.csv')

# Converter a coluna de data para datetime
df['Date'] = pd.to_datetime(df['Date'])

# Criar a pasta para salvar os gráficos
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# Adicionar colunas de semana e dia da semana
df['Semana'] = df['Date'].dt.isocalendar().week
df['Dia_da_Semana'] = df['Date'].dt.day_name()

# Agregar as vendas diárias por tipo de produto
vendas_diaria = df.groupby(['Dia_da_Semana', 'Product line'])['Total'].sum().reset_index()

# Ordenar os dias da semana
dias_da_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_diaria['Dia_da_Semana'] = pd.Categorical(vendas_diaria['Dia_da_Semana'], categories=dias_da_semana, ordered=True)
vendas_diaria = vendas_diaria.sort_values('Dia_da_Semana')

# Ajustar o tema para fundo preto completo
sns.set_theme(style="darkgrid")
plt.rcParams.update({
    "axes.facecolor": "#000000",  # Preto puro nos eixos
    "figure.facecolor": "#000000",  # Fundo preto da figura
    "grid.color": "#333333",  # Grid com cinza escuro
    "text.color": "#FFFFFF",  # Texto branco
    "xtick.color": "#FFFFFF",  # Rótulos brancos no eixo X
    "ytick.color": "#FFFFFF",  # Rótulos brancos no eixo Y
    "axes.labelcolor": "#FFFFFF",  # Cor dos rótulos dos eixos
    "legend.facecolor": "#000000",  # Fundo preto para a legenda
    "legend.edgecolor": "#FFFFFF",  # Bordas brancas na legenda
})

# Gráfico: Padrões de Compras por Dia da Semana
plt.figure(figsize=(18, 10))
sns.barplot(
    data=vendas_diaria,
    x='Dia_da_Semana',
    y='Total',
    hue='Product line',
    palette=sns.color_palette(["#D72638", "#EB5160", "#FF5700", "#FFA831", "#F7D572", "#FFFFFF"])
)

plt.title('Padrões de Compras por Dia da Semana', fontsize=22, color="#FFFFFF", weight="bold")
plt.xlabel('Dia da Semana', fontsize=16, color="#FFFFFF")
plt.ylabel('Total de Vendas (R$)', fontsize=16, color="#FFFFFF")
plt.xticks(rotation=45, fontsize=12, color="#FFFFFF")
plt.yticks(fontsize=12, color="#FFFFFF")

plt.legend(
    title='Tipo de Produto',
    fontsize=14,
    title_fontsize=16,
    frameon=True,
    edgecolor="#FFFFFF",
    facecolor="#000000",
    labelcolor="#FFFFFF"
)

plt.grid(color='#333333', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "grafico_compras_dia_semana_preto.png"), dpi=300)
plt.show()

# Gráfico: Vendas por Localização da Loja
vendas_localizacao = df.groupby(['City', 'Product line'])['Total'].sum().reset_index()

plt.figure(figsize=(18, 10))
sns.barplot(
    data=vendas_localizacao,
    x='City',
    y='Total',
    hue='Product line',
    palette=sns.color_palette(["#D72638", "#EB5160", "#FF5700", "#FFA831", "#F7D572", "#FFFFFF"])
)

plt.title('Vendas por Localização da Loja', fontsize=22, color="#FFFFFF", weight="bold")
plt.xlabel('Cidade', fontsize=16, color="#FFFFFF")
plt.ylabel('Total de Vendas (R$)', fontsize=16, color="#FFFFFF")
plt.xticks(rotation=45, fontsize=12, color="#FFFFFF")
plt.yticks(fontsize=12, color="#FFFFFF")

plt.legend(
    title='Tipo de Produto',
    fontsize=14,
    title_fontsize=16,
    frameon=True,
    edgecolor="#FFFFFF",
    facecolor="#000000",
    labelcolor="#FFFFFF"
)

plt.grid(color='#333333', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "vendas_por_localizacao_preto.png"), dpi=300)
plt.show()

    