# entrar com um valor requisitado 
# saida: saldo

def realizar_saque(valor, saldo=100.00):
    try:
        print(f"Seu saldo é: {saldo}")
        if valor > saldo: 
            raise ValueError("Nao ha saldo para completar a operacoa")
        saldo = saldo - valor
    except Exception as e:
        print(f"Algo deu errado: {e}")
    else: 
        print(f"Seu novo saldo é :{saldo}")
        
    finally:
        print("Encerrando. . .")

valor = float(input("digite o valor a solicitar: "))
realizar_saque(valor)
