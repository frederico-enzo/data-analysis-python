import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Carregar os dados
file_path = "data/vendas-tratadas.csv"  # Substitua pelo caminho correto
vendas_data = pd.read_csv(file_path)

# Ajustar a coluna de data
vendas_data['Data'] = pd.to_datetime(vendas_data['Data da fatura'])

# Criar a pasta "graficos_interativos" se não existir
output_dir = "graficos_interativos"
os.makedirs(output_dir, exist_ok=True)

# 2. Gráfico de Linha - Evolução de Vendas ao Longo do Tempo
vendas_por_dia = vendas_data.groupby('Data').agg({'Quantidade': 'sum', 'Valor': 'sum'}).reset_index()

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=vendas_por_dia['Data'], y=vendas_por_dia['Valor'], 
                          mode='lines+markers', name='Valor das Vendas',
                          line=dict(color='blue', width=2), marker=dict(size=8)))
fig1.add_trace(go.Scatter(x=vendas_por_dia['Data'], y=vendas_por_dia['Quantidade'], 
                          mode='lines+markers', name='Quantidade Vendida',
                          line=dict(color='orange', dash='dash'), marker=dict(size=8)))
fig1.update_layout(title="Evolução de Vendas ao Longo do Tempo",
                   xaxis_title="Data da Venda",
                   yaxis_title="Quantidade / Valor",
                   legend_title="Legenda",
                   hovermode="x unified")
fig1.write_html(os.path.join(output_dir, "evolucao_vendas_interativo.html"))

# 3. Histograma - Distribuição dos Valores das Vendas
fig2 = px.histogram(vendas_data, x='Valor', nbins=25, 
                    title="Distribuição dos Valores das Vendas",
                    labels={'Valor': 'Faixas de Valor (em unidades monetárias)'},
                    color_discrete_sequence=['#636EFA'])
fig2.add_vline(x=vendas_data['Valor'].mean(), line_dash="dash", line_color="red",
               annotation_text=f"Média: {vendas_data['Valor'].mean():.2f}", annotation_position="top left")
fig2.add_vline(x=vendas_data['Valor'].median(), line_dash="dot", line_color="green",
               annotation_text=f"Mediana: {vendas_data['Valor'].median():.2f}", annotation_position="top right")
fig2.update_layout(yaxis_title="Frequência", hovermode="x unified")
fig2.write_html(os.path.join(output_dir, "distribuicao_valores_interativo.html"))

# 4. Gráfico de Colunas - Vendas por Mês
vendas_data['AnoMes'] = vendas_data['Data'].dt.to_period('M')  # Extrair mês e ano
vendas_por_mes = vendas_data.groupby('AnoMes').agg({'Valor': 'sum'}).reset_index()
vendas_por_mes['AnoMes'] = vendas_por_mes['AnoMes'].astype(str)  # Converter para string para exibir no gráfico

fig3 = px.bar(vendas_por_mes, x='AnoMes', y='Valor', 
              title="Total de Vendas por Mês",
              labels={'AnoMes': 'Mês', 'Valor': 'Valor das Vendas'},
              text_auto='.2s',
              color='Valor',
              color_continuous_scale=px.colors.sequential.Blues)
fig3.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
fig3.add_scatter(x=vendas_por_mes['AnoMes'], y=vendas_por_mes['Valor'], mode='lines', 
                 line=dict(color='red', dash='dash'), name='Linha de Tendência')
fig3.update_layout(xaxis_tickangle=-45, hovermode="x unified")
fig3.write_html(os.path.join(output_dir, "vendas_por_mes_interativo.html"))

print(f"Gráficos interativos salvos na pasta: {output_dir}")
