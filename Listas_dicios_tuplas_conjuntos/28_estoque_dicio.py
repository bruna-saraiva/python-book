# criar o estoque
# criar a venda
# mostrar as vendas feitas detalhando o produto, quantidade, preco unitario e o custo
# atualizar estoque apos cada venda
# mostrar o estoque apos todas as vendas

estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50]
}
# a venda é uma lista de listas que guarda o produto comprado associado a quantidade comprada
# vendas = [["tomate", 5], ["batata", 10], ["alface", 5]]
vendas = []
while True:
    print("adicione o produto e a quantidade desejada, 'fim' para sair")
    pedido = input()
    if pedido == "fim":
        break
    # verificar se o produto existe
    if pedido not in estoque:
        print("pedido nao encontrado. proximo")
        continue
    quantidade = input()

    
    venda = [pedido, int(quantidade)]  # nova lista criada a cada iteração
    vendas.append(venda)

print(vendas)

    

total = 0
for operacao in vendas:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"Produto: {produto} | Valor Unitario: {preco} | Total: {custo} " )
    estoque[produto][0] -= quantidade
    total += custo

print(f"total vendido: {total}")
for chave, dados in estoque.items():
    print("Produto: ", chave)
    print("Quantidade:", dados[0])
    print("Valor unitario: ", dados[1])
