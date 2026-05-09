from EX_07_recursive_mdc import mdc

def mmc(a,b) -> int:
    return abs(a*b)//mdc(a,b)

a = 48
b = 18

print(f"discovering the mcd of {a} and {b} is: {mdc(a,b)}")
print(f"the mmc between {a} and {b} id: {mmc(a,b)}")