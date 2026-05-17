def fibonacci(n):
    fibo_list = [1,1]
    i = 1
    while (i < n):
        novo_item = fibo_list[i] + fibo_list[i-1]
        fibo_list.append(novo_item)
        i += 1
    return fibo_list

n = 5
print(f"the first {n} elements of fibonacci sequence are: {fibonacci(n)}")
