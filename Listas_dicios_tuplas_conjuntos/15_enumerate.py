# Para imprimirmos um indice de uma lista e seu item correspondente podemos fazer o seguinte:

array = [1,2,3]
x = 0
for item in array:
    print(f"[{x}]: {item}")
    x += 1

# Ha uma forma mais simples de fazer isso, usando enumarete.
print("------------e n u m e r a t e------------")
for z in enumerate(array):
    x, e = z
    print(f"[{x}]: {item}")
    print(z)