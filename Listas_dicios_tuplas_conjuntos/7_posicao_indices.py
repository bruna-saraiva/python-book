# le cinco numeros, armazena-os em uma lista e solicita que o usuario escolha a posicao que quer para imprimir
lista = []
x = 0
while x < 5:
    items = int(input(f"Insert[{x+1}]: "))
    lista.append(items)
    x += 1

print(f"Choose the position of the number you want to print 1 a 5")
posicao = int(input()) - 1
print(f"Numero de posicao {posicao}: {lista[posicao]}")


