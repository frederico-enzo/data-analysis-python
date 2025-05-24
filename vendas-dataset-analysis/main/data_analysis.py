import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados
file_path = "data/vendas-tratadas.csv"  # Substitua pelo caminho correto
vendas_data = pd.read_csv(file_path)

# Ajustar a coluna de data (substitua 'Data da fatura' pelo nome correto)
vendas_data['Data'] = pd.to_datetime(vendas_data['Data da fatura'])

# Criar a pasta "graficos" se não existir
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# 2. Gráfico de Linha - Evolução de Vendas ao Longo do Tempo
vendas_por_dia = vendas_data.groupby('Data').agg({'Quantidade': 'sum', 'Valor': 'sum'}).reset_index()

plt.figure(figsize=(12, 6))
plt.plot(vendas_por_dia['Data'], vendas_por_dia['Valor'], label='Valor das Vendas', marker='o', linestyle='-')
plt.plot(vendas_por_dia['Data'], vendas_por_dia['Quantidade'], label='Quantidade Vendida', marker='x', linestyle='--')
plt.title('Evolução de Vendas ao Longo do Tempo', fontsize=16)
plt.xlabel('Data da Venda', fontsize=14)
plt.ylabel('Quantidade / Valor', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "evolucao_vendas.png"))
plt.close()

# 3. Histograma - Distribuição dos Valores das Vendas
plt.figure(figsize=(12, 6))
plt.hist(vendas_data['Valor'], bins=20, color='orange', edgecolor='black', alpha=0.7)
plt.title('Distribuição dos Valores das Vendas', fontsize=16)
plt.xlabel('Faixas de Valor (em unidades monetárias)', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "distribuicao_valores.png"))
plt.close()

# 4. Gráfico de Colunas - Vendas por Mês
vendas_data['AnoMes'] = vendas_data['Data'].dt.to_period('M')  # Extrair mês e ano
vendas_por_mes = vendas_data.groupby('AnoMes').agg({'Valor': 'sum', 'Quantidade': 'sum'}).reset_index()
vendas_por_mes['AnoMes'] = vendas_por_mes['AnoMes'].astype(str)  # Converter para string para exibir no gráfico

plt.figure(figsize=(12, 6))
plt.bar(vendas_por_mes['AnoMes'], vendas_por_mes['Valor'], color='skyblue', label='Valor Total')
plt.title('Total de Vendas por Mês', fontsize=16)
plt.xlabel('Mês', fontsize=14)
plt.ylabel('Valor das Vendas', fontsize=14)
plt.xticks(rotation=45)
plt.legend(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "vendas_por_mes.png"))
plt.close()

print(f"Gráficos salvos na pasta: {output_dir}")
