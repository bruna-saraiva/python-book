# def mdc(a,b):
#     # verificar
#     # divide the bigger one by the smaller one
#     # guardar o resto 
#     # atribuir o resto ao maior 
#     # quando o resto for zero entao o resto anterior é o valor 
#     resto = 1
#     while (resto != 0):

#         resto = a % b
#         print(resto)
#         a = b 
#         print(a)
#         b = resto
#         print(b) 

#     return a





def mdc(a, b):

    resto = a % b
    if resto == 0:
        print(f"o a final é {b}")
        return b
    else:
        print(f"a era {a}")
        print(f"b era {b}")
        a = b
        b = resto
        print(f"agora a é {a}")
        print(f"e b é {b}")
        return mdc(a, b)  # Adicionado return para a chamada recursiva


a = 48
b = 18

print(f"discovering the mcd of {a} and {b} is: {mdc(a,b)}")
