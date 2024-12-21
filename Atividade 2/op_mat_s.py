# Solicitando como entrada dois números e depois vamos realizar uma operação simples entre eles. (utilizando GitHub Copilot)

# Solicitando os números

input1 = float(input("Digite o primeiro número: "))
input2 = float(input("Digite o segundo número: "))

input3 = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Realizando a operação

if input3 == "+":
    resultado = input1 + input2

elif input3 == "-":
    resultado = input1 - input2

elif input3 == "*":
    resultado = input1 * input2

elif input3 == "/":
    resultado = input1 / input2

else:
    resultado = "Operação inválida"

# Printando o resultado
print("O resultado da operação é: ", resultado)

# Fim