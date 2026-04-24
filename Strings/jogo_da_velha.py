matriz = [["   ","   ","   "],["   ","   ","   "],["   ","   ","   "]]
posicoes = [
    (0, 0), (0, 1), (0, 2), # 1, 2, 3
    (1, 0), (1, 1), (1, 2), # 4, 5, 6
    (2, 0), (2, 1), (2, 2)  # 7, 8, 9
]
jogador1 = "Bruna"
jogador2 = "Nat"

pos_escolhidas = []
for i in range(3):
    print("".join(matriz[i]))
    print("---+---+---")


rodada = 0
# vou precisar de uma variavel jogada para receber o local da matriz para marcar
while rodada < 9:
    print("----------------------------------------")
    escolha = int(input("Escolha de 1 a 9: "))
    
    if escolha in pos_escolhidas:
        print("EPA, essa posicao ja foi escolhida, tente outra")
        continue
    else:
        pos_escolhidas.append(escolha)
        linha, coluna = posicoes[escolha - 1]

        if rodada % 2 == 0:
            print(f"{jogador1} joga (X)")
            matriz[linha][coluna] = " X "
        else: 
            print(f"{jogador2} joga (0)")
            matriz[linha][coluna] = " 0 "
        

        for i in range(3):
            print("|".join(matriz[i]))
            print("---+---+---")
        
        rodada = rodada + 1

print('fim de jogo----------------------------------')




