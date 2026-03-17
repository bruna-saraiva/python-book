# podemos usar len(lista) para encontrar o tamanho de uma lista, vamos usar isso em um programa que mostra os itens de uma lista
L = [1,2,3]
x = 0

while x < len(L):
    print(L[x])
    x += 1

# A vantagem é que podemos alterar L para o tamanho que quisermos, sem ter que mudar o limite no laço
# Observe uqe o numero retornado por len(L) nao pode ser usado como indice, pois o retorno sera o quantidade exata de itens que compoem a lista, no caso é 3
