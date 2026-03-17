# podemos utilizar lista.append(item) para adicionar um item a uma lista, isso se chama metodo e podemos usa-lo porque uma lista é um objeto
L = [1,2,3]
L.append(4)
print(L)
# se voce adicionar uma lista em append, olhar o que acontece
L.append([1,2])
print(L) # voce cria uma lista dentro de outro, ela é adicionada como apenas um elemento
# podemos adicionar numeros a uma lista simplesmente concatenando-a com outra
L = L + [1,5] # isso é semelhante a usar L.extend([1,5])
print(L)
# com isso, crie um programa que le numeros ate 0 ser digitado para sair, depois imprime os numeros na mesma ordem que foram inseridos
lista = []
x = 0
while True:
    item = int(input("insira um numero: "))

    if item == 0:
        break
    lista.append(item)

while x < len(lista):
    print(f"numero {x+1}: {lista[x]}")
    x += 1
