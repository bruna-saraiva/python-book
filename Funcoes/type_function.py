# printar o tipo de elementos de uma lista

L = [2, "hello", ["!"], {"a": 1, "b": 2}]

def identify_types(L):
    for e in L:
        print(type(e))

# identify_types(L)

# navegar em uma lista, printar direto se for string, se for lista imprimir cada elemento 
L_2 = ["a", ["b", "c", "d"], "e"]

# iterar sobre a lista, verificar se é string, se for printa, se for lista iterar novamente 

def navigate_lists(L):
    for e in L:
        if type(e) is str: 
            print("string")
            print(e)
        else:
            print("navigating into list")
            for element in e:
                print(element)

# navigate_lists(L_2)

# escreva uma funcao recursiva que imprima elementos de uma lista. cada elemento deve ser impresso por linha. 
# a cada nivel imprima a lista mais a direita como fazemos para identar blocos 
# dica: envie o nivel atual como parametro e utilize-o para calcular a qtd de brancos

L_3 = [1,[2,3,4, [5,6,7]]]

def navigate_recursively(L,white_spaces):
    for e in L:
        if type(e) != list:
            spaces = " " * white_spaces
            print(f"{spaces}{e}")
        else:
            white_spaces += 1
            navigate_recursively(e, white_spaces)

navigate_recursively(L=L_3, white_spaces=0)

