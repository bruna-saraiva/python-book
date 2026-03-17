temps = [-10,-8,0,1,2,5,-2,-4]
max = temps[0]
min = temps[0]

sum = 0

for e in temps:
    if e > max:
        max = e
    
    elif e < min:
        min = e

    sum = sum + e

print(f"a menor temp foi {min}, a maior foi {max}")
print(f" a media das temperaturas foi {sum/len(temps)}")