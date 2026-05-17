# Jogo da forca ----------------------------------------------------------------------------
import random
# palavra = input("Insira a palavra do jogo da forca: ").lower().strip()
palavras = ["ana", "roupeiro", "paralelepipedo", "helicoptero"]
# numero = int(input("escolha um numero: "))
# indice = (numero * 773) % len(palavras)
indice = random.randint(0,3)
print(f"o indicie escolhido foi {indice}")
palavra = palavras[indice]
# for i in range(100):
#     print("")

erros = 0
digitadas = []
acertadas = []
linhas = []
linha1 = []
linha2 = []
linha3 = []

# eu termino o jogo quando a palavra_a_preencher for == a palavra e quando ultrapasso meu limite de erros
while True: 
    palavra_a_preencher = "" # por que nao posso criar ela la fora? 
    for letra in palavra: 
        if letra in acertadas:
            palavra_a_preencher += letra
        else:
            palavra_a_preencher += "*"
    print("A palavra esta atualmente assim: ", palavra_a_preencher)
    if palavra_a_preencher == palavra:
        print("voce acertou!")
        break

    letra_chute = input("digite sua letra de chute: ").lower().strip()

    if letra_chute in digitadas:
        print("opa, essa letra ja foi digitada, tente outra!")
        continue # vai voltar la pra cima
    else:
        digitadas += letra_chute
        if letra_chute in palavra:
            acertadas.append(letra_chute)
        else:
            print("voce errou")
            erros += 1
        # print("X==:==\nX  :  ")
        # print("X  O  " if erros >= 1 else "X")
        # linha2 = ""
        # if erros == 2:
        #     linha2 = "  |  "
        # elif erros == 3: 
        #     linha2 = " \\|  "
        # elif erros >= 4:
        #     linha2 = " \\|/ "
        # print(f"X{linha2}")
        # linha3 = ""
        # if erros == 5:
        #     linha3 += " /  "
        # elif erros >= 6:
        #     linha3 += " / \\ "
        # print(f"X{linha3}")
        # print("X\n============")   
        
        if erros == 1:
            linha1.append(" O")
        elif erros == 2: 
            linha2.append("\\")
        elif erros == 3: 
            linha2.append("|")
        elif erros == 4:
            linha2.append("/")
        elif erros == 5:
            linha3.append("/ ")
        elif erros == 6:
            linha3.append("\\")
        
        
        print("".join(linha1))
        print("".join(linha2))
        print("".join(linha3))
  
        if erros > 6:
            print(f"a palavra era {palavra}")
            print("voce perdeu")
            break
        
    



        

