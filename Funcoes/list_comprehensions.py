# transformar itens de uma lista em uma tupla (elemento, seu dobro) com list comprehensions

L = [0, 1, 2, 3, 4]

def list_to_tuple_double(L):
    L_double = [(x,x * 2) for x in L]
    return L_double

# colocar apenas numeros pares em uma lista
def only_evens():
    L = [x for x in range(10) if x % 2 == 0]
    return L

# print(list_to_tuple_double(L))
print(only_evens())