# LER DUAS STRINGS
# GERAR UMA TERCEIRA COM OS CARACTERES COMUNS AS DUAS STRINGS
# USAE O FIND E O RFIND
s_um = str(input("insira a string: "))
print(s_um)
s_dois = str(input("insira a segunda string: "))
print(s_dois)

s_tres = []
# s_dois = list(s_dois)
for caractere in s_dois:
    if caractere in s_um:
        print(f"achei um em comum {caractere}")
        s_tres.append(caractere)

s_tres = "".join(s_tres)
print(s_tres)
