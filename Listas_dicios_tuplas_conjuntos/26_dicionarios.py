# criacao de um dicionario
tabela = {
    "maca": 0.45,
    "banana": 0.10,
    "laranja": 0.20
}

# para acessar um valor de uma chave
print(tabela["banana"])

# criar uma nova chave sem entrar no dicionario
tabela["cebola"] = 1.20
print(tabela)

# verifique se uma chave existe
print("manga" in tabela)
print("laranja" in tabela)
# transformar as chaves em uma lista
chaves = list(tabela.keys())
print(chaves)
# transformar os valores 
valores = list(tabela.values())
print(valores)