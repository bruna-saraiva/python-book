# Programa
'''
O programa deve ter uma lista onde cada item representa a quantidade de vagas
numa sala de cinema, cada indice da lista representa uma sala. 
1 - Pedir o numero da  sala e verificar se tem lugar vago nela (alem de verificar se o numero e valido p
quantidade de vagas)
2 - Pedir a quantidade de lugares
3 - verificar se a qtd de vagas solicitada para a sala tem disponivel
4 - retirar lugares da sala 
5 - exibir nova quantidade 
'''

lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("entre com o numero da sala(1 a 5)"))

    if sala == 0:
        print("fim")
        break

    if sala > len(lugares_vagos) or sala < 0:
        print("sala inexistente, tente outra")
    
    elif lugares_vagos[sala - 1] == 0: 
        print("sala lotada")
    else:
        lugares = int(input("insira a quantidade de lugares"))
        if lugares > lugares_vagos[sala - 1]:
            print("nao existem lugares suficientes")
        elif lugares < 0: 
            print("quantidade inválida")
        else:
            lugares_vagos[sala - 1] -= lugares
        
for x, l in enumerate(lugares_vagos):
    print(f"sala{x + 1} possui {l} lugares")
    
