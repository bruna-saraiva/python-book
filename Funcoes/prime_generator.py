def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def generate_n_primes(n):
    i = 0
    j = 2
    while i < n:
        if is_prime(j):
            yield j
            i+=1
        j+=1

prime_numbers = [x for x in generate_n_primes(10)]
print(prime_numbers)