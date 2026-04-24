# LER DUAS STRINGS
# GERAR UMA TERCEIRA COM OS CARACTERES DISJUNTOS
# USAE O FIND E O RFIND
s_um = "CTA"
print(s_um)
s_dois = "ABC"
print(s_dois)

s_tres = []
# s_dois = list(s_dois)
for caractere in s_dois:
    if caractere not in s_um:
        print(f"achei um disjunt! é o {caractere}")
        s_tres.append(caractere)
for caractere in s_um:
    if caractere not in s_dois:
        print(f"achei um disjunt! é o {caractere}")
        s_tres.append(caractere)

s_tres = "".join(s_tres)
print(s_tres)
