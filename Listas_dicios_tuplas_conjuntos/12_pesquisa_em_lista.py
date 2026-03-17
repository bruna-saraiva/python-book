lista = [15, 7, 27, 39]
procurado_1 = int(input("digite o valor que quer procurar:"))
procurado_2 = int(input("digite o outro valor que quer procurar:"))
x = 0
count = 0
primeiro = 0
while x < (len(lista)):
    if lista[x] == procurado_1: 
        print(f"item {procurado_1} encontrado em posicao {x}")
        if count == 0:
            print("procurado 1 foi o primeiro a ser encontrado")
        count += 1
        
        
    elif lista[x] == procurado_2:
        print(f"item{procurado_2} encontrado em posicao {x}")
        if count == 0:
            print("procurado 2 foi o primeiro a ser encontrado")
        count += 1
        

    if count == 2:
        print("usando break!!")
        break
    x += 1

if count == 0:
    print("item nao encontrado")