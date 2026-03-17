# crie um programa de empilhar ou desempilhar pratos
qtd_pratos = 5
pilha = list(range(1,qtd_pratos + 1)) # vai ser [1,2,3,4,5]

# E para empilhar, D para desempilhar e S para sair
while True: 
    print(f"pilha de pratos{pilha}")

    operacao = str(input("escolha a operacao (E - empilha, D - desempilha, S - sair): "))

    if operacao == "E":
        qtd_pratos +=1
        print("empilhando")
        pilha.append(qtd_pratos)

    elif operacao == "D":
        if len(pilha) > 0:
            print("desempilhando")
            pilha.pop(-1) # retiro o ultimo que entrou
        else:
            print("pilha vazia")
    elif operacao == "S":
        print("encerrando")
        break
    else:
        print("entrada invalida")

