# Copiando uma lista
L = [1,2,3,4,5]
V = L
print(L)
print(V)
# dessa forma vemos que essas listas sao iguais, se tentarmos transformar um item da copia da lista veja o que acontece
# V[0] = 6
# print(L)
# print(V)
# uma lista é um objeto, se fizermos uma copia, iremos apenas criar outra variavel que aponta para o mesmo objeto
# para isso nao acontecer devemos mudar a sintaxe assim:
V = L[:]
V[0] = 6
print(L)
print(V)

# podemos tambem fatiar as strings para transformar em outras
print("Isso mostra a string do começo ao fim: ",L[0:5])
print("isso tambem: ", L[:5])
print("Isso mostra a string sem o ultimo item", L[:-1])
print("Isso mostra um intervalo entre os itens da string, observe que antes do : é incio e depois é fim", L[1:3])
print("Aqui eu mostro da 4 posicao ate o fim", L[3:])
print("Assim eu posso mostrar os indices de tras pra frente", L[-2])
