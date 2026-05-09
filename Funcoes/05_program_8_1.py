# funcao do programa 8_1 feito no livro 
def pesquise(lista,valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
    return None

def pesquise_b(lista,valor):
    lista= ",".join(map(str,lista))
    valor = str(valor)
    return lista.find(valor)

L= [10,20,25,30]

print(pesquise_b(L,25))

