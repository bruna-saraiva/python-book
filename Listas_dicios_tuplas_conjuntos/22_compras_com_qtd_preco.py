compras = []

while True:
    produto = str(input("insira o produto: "))
    if produto == "fim":
        break

    quantidade = int(input("insira a quantidade: "))
    preco = float(input("insira o preco: "))
    compras.append([produto, quantidade, preco])
    
soma = 0
for item in compras:
    total_produto = item[1] * item[2]
    print(f"produto: {item[0]}| total: {item[1]} x {item[2]} = {total_produto}")
    soma = soma + total_produto
    
print(f"total compra: {soma}")

