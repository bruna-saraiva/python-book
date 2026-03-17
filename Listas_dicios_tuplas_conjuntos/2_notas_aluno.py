# Calculo da media
notas = []

soma = 0
x = 0 
# while x < len(notas):
#     soma+=notas[x]
#     x+=1
# receber as notas
while x < 5:
    # notas[x] = float(input(f"Nota{x}: "))
    nota = float(input(f"Notas{x}: "))
    notas.append(nota)
    soma += notas[x]
    x+=1

x = 0

# mostrar notas
while x <len(notas):
    print(f"Nota{x}:{notas[x]:.2f}")
    x+=1
print(f"A média é {soma/x:.2f}")
