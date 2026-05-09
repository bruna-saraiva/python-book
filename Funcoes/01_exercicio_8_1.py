# escrever uma funcao que retorne o maior de dois elementos
# vai receber dois parametros ne
a = int(input("preencha o primeiro elemento"))
b = int(input("preencha o segundo elemento"))


def maximo(a,b):
    maximo = 0
    if a > b:
        maximo = a
    else:
        maximo = b
    
    return maximo 

print(f"o maior elemento é o {maximo(a,b)}")