# calculando a média de três notas fornecidas na entrada do usuário.

# Solicita as três notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print(f"A média das notas é: {media:.2f}")