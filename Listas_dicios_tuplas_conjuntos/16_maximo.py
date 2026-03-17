array = [1,5,0,2,1]
max = array[0]

for x, e in enumerate(array):
    if e > max:
        max = e
        pos = x

print(f"o maximo é {max} na posicao {pos}")    
