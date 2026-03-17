lista = [1,2,3,4,5]
fim = len(lista)
while fim > 1:
    x = 0
    trocou = False
    while x < (fim - 1):
        if lista[x] <  lista[x+1]:
            trocou = True
            temp = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = temp
        x = x + 1
    if not trocou:
        break
    fim = fim - 1
print("Numeros ordenados:")
print(lista)
