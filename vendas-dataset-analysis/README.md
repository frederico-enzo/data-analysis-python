# Análise de Vendas

Este projeto visa a análise de dados de vendas utilizando gráficos interativos, desenvolvidos com a biblioteca **Plotly**. Ele permite visualizar a evolução das vendas ao longo do tempo, a distribuição dos valores de vendas e o total de vendas por mês, tudo de forma dinâmica e interativa.

## Funcionalidades

1. **Evolução de Vendas ao Longo do Tempo**  
   Um gráfico de linha que mostra a evolução do valor das vendas e a quantidade vendida ao longo do tempo, permitindo identificar tendências e picos de vendas.

2. **Distribuição dos Valores das Vendas**  
   Um histograma interativo que exibe a distribuição dos valores das vendas, com destaque para a média e a mediana. Esse gráfico ajuda a entender melhor os padrões de preços das vendas realizadas.

3. **Vendas por Mês**  
   Um gráfico de barras que exibe o total de vendas por mês, com uma linha de tendência para ajudar a identificar picos e quedas nas vendas ao longo do tempo.

## Arquivos Gerados

- **Gráficos Interativos em HTML**  
  Após rodar o código, os gráficos são gerados como arquivos HTML interativos que podem ser abertos diretamente no navegador para exploração detalhada.

  - [Evolução de Vendas ao Longo do Tempo](graficos_interativos/evolucao_vendas_interativo.html)
  - [Distribuição dos Valores das Vendas](graficos_interativos/distribuicao_valores_interativo.html)
  - [Vendas por Mês](graficos_interativos/vendas_por_mes_interativo.html)

## Como Executar

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu_usuario/analise_vendas.git


2. Instale as dependências necessárias:
   ```bash
    pip install -r requirements.txt

3. Execute o script analisar_vendas.py:
   ```bash
    python analisar_vendas.py

## Dependências
  - pandas
  - plotly
  - numpy
