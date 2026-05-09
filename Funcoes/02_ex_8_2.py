# escrever uma funcao que retorne true se o primeiro numero for multiplo do seugndo 

a = int(input("preencha o primeiro elemento"))
b = int(input("preencha o segundo elemento"))

def multiplo(a,b):
    if a % b == 0:
        return True
    else:
        return False

print(f"{a} é multiplo de {b}: {multiplo(a,b)}")