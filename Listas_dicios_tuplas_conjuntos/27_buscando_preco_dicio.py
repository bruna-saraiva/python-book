# obter o preco de um produto no dicionario
tabela = {
    "alface" : 0.45,
    "batata" : 1.20,
    "tomate" : 2.30,
    "feijao" : 1.50
}

while True:
    produto = input("Digite o nome do produto para saber o seu preco, digite fim para terminar: ")
    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço do {produto}: R$ {tabela[produto]}")
    else:
        print("produto nao encontrado")
