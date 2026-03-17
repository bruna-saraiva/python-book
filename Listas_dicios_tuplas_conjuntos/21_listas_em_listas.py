# podemos acessar strings dentro da lista, letra a letra, usando um segundo indice
S = ["macas", "peras", "kiwis"]
print(S[0][0])
# vai imprimir M
print("imprimindo todo o texto")
for s in S:
    for letra in s: 
        print("letra") # mudei pra "letra" so pra nao encher o temrinal
        # vai imprimir todas as palavras

# lista com elementos de tipos de diferentes
produto1 = ["macas", 10, 0.3]
produto2 = ["peras", 3., 0.75]
produto3 = ["kiwis", 2, 0.98]

compras = [produto1, produto2, produto3]
print(compras)

# imprimindo elementos das compras separadamente
for e in compras:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]}")