''' faca um programa que leia duas listas e 
que gere uma terceira com os elementos das duas primeiras
''' 
lista1 = [1, 2]
lista2 = [2, 4, 1]

lista3 = []
lista3 = lista1 + lista2
print(lista3)

'''Faca um codigo que percorra duas listas e gere uma terceira sem elementos repetidos'''

lista4 = []
for item in lista1:
    if item not in lista4:
        lista4.append(item)

for item in lista2:
    if item not in lista4:
        lista4.append(item)

print(lista4)