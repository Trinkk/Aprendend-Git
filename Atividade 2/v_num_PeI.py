# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. (utilizando GitHub Copilot)

# Verificando paridade

def verificar_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Entrando com um número inteiro e verificando se ele é par ou ímpar

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = verificar_paridade(numero)
        print(f"O número {numero} é {resultado}.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")