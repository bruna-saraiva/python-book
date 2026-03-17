# faca um programa que leia uma string(compra) e depois exiba as compras

compras = []

while True:
    compra = str(input("digite o item que deseja comprar(0 para sair):"))
    if(compra == "0"):
        print("finalizando")
        break
    else:
        print(f"inserindo {compra} na lista de compras")
        compras.append(compra)

print("---------- compras ----------")
for x,c in enumerate(compras):
    print(f"{x} : {c}")
