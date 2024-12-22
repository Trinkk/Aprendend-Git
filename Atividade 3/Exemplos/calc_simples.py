# Calculadora simples em Python

def somar(a, b):
    """Função que soma dois números."""
    return a + b

def subtrair(a, b):
    """Função que subtrai dois números."""
    return a - b

def multiplicar(a, b):
    """Função que multiplica dois números."""
    return a * b

def dividir(a, b):
    """Função que divide dois números. Retorna erro se o denominador for zero."""
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b

def calculadora():
    """Função principal da calculadora."""
    print("Bem-vindo à Calculadora!")
    print("Selecione a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    # Solicita a escolha do usuário
    escolha = input("Digite o número da operação: ")

    # Verifica se a entrada é válida
    if escolha not in ["1", "2", "3", "4"]:
        print("Ops... essa opção é inválida. Tente novamente!")
        return

    # Solicita os números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza a operação escolhida
    if escolha == "1":
        print(f"Resultado: {somar(num1, num2)}")
    elif escolha == "2":
        print(f"Resultado: {subtrair(num1, num2)}")
    elif escolha == "3":
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif escolha == "4":
        print(f"Resultado: {dividir(num1, num2)}")

# Chama a função principal
calculadora()