'''Se usarmos o "for" no programa 5_adicao_elementos no lugar do while nao conseguiremos 
substituir o primeiro while, porque nao sabemos quantas vezes esse loop deve se repetir'''
array = []
while True:
    item = int(input("insert item: "))
    array.append(item)

    if item == 0:
        break

for item in array:
    print(item)