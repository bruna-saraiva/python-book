# crie um programa que leia uma expressao de parenteses usando pilhas verifique se os parenteses foram abertos e fechdos na ordem correta
# adicione elementos a pilha sempre que ele for um abre parenteses e desempilhe sempre que for um )


expressao = str(input())
pilha = []
valido = True
for item in expressao:
    if item == '(':
        pilha.append(item)
    
    elif item == ')':
        if len(pilha) == 0:
            valido = False
            break
        else:
            pilha.pop(-1)
            

if len(pilha) == 0 and valido == True:
    print("oK")
else:
    print("ERRO")


    
    
            
    

