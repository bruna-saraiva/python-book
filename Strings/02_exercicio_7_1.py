# Ler duas Strings
# Verificar se a segunda ocorre dentro da primeira
# Encontrar a posicao de inicio

s_um = str(input("insira a string: "))
print(s_um)
s_dois = str(input("insira a segunda string: "))
print(s_dois)
ocorrencia = s_um.find(s_dois, 0)

print(ocorrencia)
if ocorrencia >= 0: 

    print(f"encontrada na posicao {ocorrencia}")
else:
    print("nao foi encontrada")