# LER UMA STRIN
# verificar os caracteres 
# contar os caracteres
# transformar a stirng em set? 
s = "TTAAC"
s_set = set(s)

for item in s_set:
    contagem = s.count(item)
    print(f"contagem de {item}: {contagem}")
