import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_csv('supermarket-sales-dataset/data/sales-dataset.csv')

# Converter a coluna de data para datetime
df['Date'] = pd.to_datetime(df['Date'])

# Criar a pasta para salvar os gráficos
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# Adicionar colunas de semana e dia da semana
df['Semana'] = df['Date'].dt.isocalendar().week
df['Dia_da_Semana'] = df['Date'].dt.day_name()

# Agregar as vendas por localização
vendas_localizacao = df.groupby(['City'])['Total'].sum().reset_index()

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

# Gráfico de Pizza: Vendas por Localização da Loja
plt.figure(figsize=(10, 10))
# Usando cores com tons de vermelho
colors = sns.color_palette(["#D72638", "#EB5160", "#FF5700", "#FF6F61", "#F7A400", "#D43F00", "#F77F00"])

# Plotando o gráfico de pizza
plt.pie(
    vendas_localizacao['Total'], 
    labels=vendas_localizacao['City'], 
    autopct='%1.1f%%', 
    colors=colors, 
    startangle=140, 
    wedgeprops={'edgecolor': 'white'}
)

plt.title('Vendas por Localização da Loja', fontsize=22, color="#FFFFFF", weight="bold")
plt.axis('equal')  # Para garantir que o gráfico seja circular

# Salvar o gráfico como imagem
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "vendas_por_localizacao_pizza.png"), dpi=300)
plt.show()
