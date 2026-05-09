# escrever uma funcao que retorne a area de um triangulo
base = int(input("preencha com a base do tri: "))
altura = int(input("preencha com a altura do tri: "))

def triangulo(base,altura):
    return (base * altura) /2
    
print(f"a area do triangulo é {triangulo(base,altura)}")