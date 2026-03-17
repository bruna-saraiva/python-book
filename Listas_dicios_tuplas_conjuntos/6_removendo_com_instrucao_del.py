# del é uma instrucao que podemos usar para remover um item especifico da lista
L = [1, 2, 3]
del L[1]
print(L)

L = list(range(101))# a funcao range retorna numeros em sequencia a cada chamada e list agrupa-os em uma lista como se tivesse fazendo um for e append
del L[1:99]
print(L)