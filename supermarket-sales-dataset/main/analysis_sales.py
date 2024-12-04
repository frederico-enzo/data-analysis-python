import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('supermarket-sales-dataset\data\sales-dataset.csv')

df['Date'] = pd.to_datetime(df['Date'])

output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# Adicionar colunas de semana e dia da semana
df['Semana'] = df['Date'].dt.isocalendar().week
df['Dia_da_Semana'] = df['Date'].dt.day_name()

# Agregar as vendas semanais por tipo de produto e localização
vendas_semanal = df.groupby(['Semana', 'Product line', 'City'])['Total'].sum().reset_index()

# Análise de padrões de compras por dia da semana (ex: vendas mais altas em feriados ou fins de semana)
vendas_diaria = df.groupby(['Dia_da_Semana', 'Product line'])['Total'].sum().reset_index()

# Comparação de desempenho entre diferentes categorias de produtos
vendas_categoria = df.groupby(['Product line'])['Total'].sum().reset_index()

# Análise de vendas por localização da loja
vendas_localizacao = df.groupby(['City', 'Product line'])['Total'].sum().reset_index()

# Gráfico de vendas semanais por tipo de produto
plt.figure(figsize=(20, 10))
sns.lineplot(data=vendas_semanal, x='Semana', y='Total', hue='Product line', marker='o', palette='Set2')
plt.title('Vendas Semanais por Tipo de Produto', fontsize=16)
plt.xlabel('Semana', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='Tipo de Produto', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "vendas_semanais_tipo_produto.png"))
plt.show()

# **Storytelling para o gráfico de vendas semanais**: 
# Este gráfico mostra como as vendas de diferentes categorias de produtos variam ao longo das semanas. 
# Isso ajuda a identificar tendências de compra ao longo do tempo, como picos de vendas em certas semanas, 
# o que pode estar relacionado a promoções, feriados ou sazonalidade.

# Gráfico de Padrões de Compras por Dia da Semana
plt.figure(figsize=(20, 10))
sns.barplot(data=vendas_diaria, x='Dia_da_Semana', y='Total', hue='Product line', palette='Set2')
plt.title('Padrões de Compras por Dia da Semana', fontsize=16)
plt.xlabel('Dia da Semana', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='Tipo de Produto', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "padrões_compras_dia_semana.png"))
plt.show()

# **Storytelling para o gráfico de padrões de compras por dia da semana**:
# Este gráfico revela como o comportamento de compra dos consumidores varia ao longo da semana. 
# Podemos ver se as vendas são mais altas em finais de semana, quando muitos consumidores têm mais tempo 
# para fazer compras, ou se há algum pico em dias específicos, como segunda-feira, que pode estar relacionado 
# ao início da semana de trabalho.

# Gráfico de Comparação de Desempenho por Categoria de Produto
plt.figure(figsize=(20, 10))
sns.barplot(data=vendas_categoria, x='Product line', y='Total', palette='Set2')
plt.title('Comparação de Desempenho entre Categorias de Produto', fontsize=16)
plt.xlabel('Categoria de Produto', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "desempenho_categoria_produto.png"))
plt.show()

# **Storytelling para o gráfico de comparação entre categorias de produtos**:
# Aqui, podemos comparar como diferentes categorias de produtos se desempenham no total de vendas. 
# Isso permite observar quais categorias de produtos estão dominando as vendas e quais podem precisar de mais 
# atenção em termos de promoções ou estratégias de marketing.

# Gráfico de Vendas por Localização da Loja
plt.figure(figsize=(20, 10))
sns.barplot(data=vendas_localizacao, x='City', y='Total', hue='Product line', palette='Set2')
plt.title('Vendas por Localização da Loja', fontsize=16)
plt.xlabel('Cidade', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='Tipo de Produto', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "vendas_por_localização.png"))
plt.show()

# **Storytelling para o gráfico de vendas por localização da loja**:
# Esse gráfico mostra como as vendas variam de acordo com a localização da loja, o que pode indicar 
# diferenças regionais no comportamento de compra. Algumas cidades podem mostrar maior demanda por certas 
# categorias de produtos, influenciando o planejamento de estoque e campanhas direcionadas para diferentes regiões.

