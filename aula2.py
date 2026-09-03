# PRÁTICA 02
# Primeiro programa aplicado a negócios

# Dados
produto = "Monitor"
preco = 1800.00
quantidade = 7
cliente_ativo = True
percentual_desconto = 12
percentual_comissao = 5
custo_unitario = 1250

# Processamento
total_venda = preco * quantidade
valor_desconto = total_venda * percentual_desconto / 100
valor_final = total_venda - valor_desconto
valor_comissao = total_venda * percentual_comissao / 100
custo_total = custo_unitario * quantidade
lucro_bruto = valor_final - custo_total

# Saída
print("Meu primeiro programa aplicado a negócios")
print(produto)
print(preco)
print(quantidade)
print(cliente_ativo)
print(type(produto))
print(type(preco))
print(type(quantidade))
print(type(cliente_ativo))
print(total_venda)
print(valor_desconto)
print(valor_final)
print("Produto:", produto)
print("Preço unitário:", preco)
print("Quantidade:", quantidade)
print("Total da venda:", total_venda)
print("Desconto:", valor_desconto)
print("Valor final:", valor_final)
print("Comissão:", valor_comissao)
print("Custo total:", custo_total)
print("Lucro bruto:", lucro_bruto)