# corrigir o programa 8.2
def soma(L):
    total = 0
    x = 0
    while x < 5:
        total += L[x]
        x += 1
    return total

L = [1,7,2,9,15]
# print(soma(L))

# como eu faria
def soma_b(L):
    total = 0
    for item in L:
        total += item
    return total
print(soma_b(L))