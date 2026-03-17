'''Crie uma fila:
a lista representara os clientes e o numero de 1 a 10 representara a ordem de chegada deles
o programa deve representar um sistema que A - atende o cliente ( remove da fila)
F - coloca alguem na fila
S - encerra os atendimentos 

'''
ultimo = 10
fila = list(range(1, ultimo + 1)) # vai criar uma lista de 1 a 10, se eu nao adicionasse 1 ali, ficaria 9

# vamos comecar os atedimentos 
while True:
    print(f"fila atual: {fila}")
    operacoes = str(input("entre com a operacao(A - atender, F - entrar na fila, S - encerrar: )"))

    for operacao in operacoes:
        if operacao == "A":
            if len(fila) > 0: 
                print("Atendendo cliente: ", fila.pop(0)) 
        
            else:
                print("fila vazia . . .")

        elif operacao == "F":
            print("adicionando novo cliente na fila")
            ultimo = ultimo + 1
            fila.append(ultimo)
        
        elif operacao == "S":
            print("encerando expediente . . .")    
            break
        else: 
            print("operacao invalida")

