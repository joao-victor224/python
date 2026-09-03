# DESAFIO FINAL

# Dados
quantidade = 25
preco_unitario = 120.00
custo_unitario = 75.00
percentual_desconto = 5

# Processamento
valor_bruto = preco_unitario * quantidade
valor_desconto = valor_bruto * percentual_desconto / 100
valor_final = valor_bruto - valor_desconto
custo_total = custo_unitario * quantidade
lucro_bruto = valor_final - custo_total

# Saída
print("Valor bruto da venda:", valor_bruto)
print("Valor do desconto:", valor_desconto)
print("Valor final da venda:", valor_final)
print("Custo total:", custo_total)
print("Lucro bruto:", lucro_bruto)