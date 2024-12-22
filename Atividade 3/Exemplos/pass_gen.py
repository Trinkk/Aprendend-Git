# Gerador de Senhas Aleatórias

import random
import string

def gerar_senha(tamanho):
    """Gera uma senha aleatória com o tamanho especificado."""
    # Define os caracteres disponíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gera a senha usando uma escolha aleatória para cada caractere
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Solicita o tamanho da senha ao usuário
tamanho_senha = int(input("Digite o tamanho da senha desejada: "))

# Gera e exibe a senha
senha = gerar_senha(tamanho_senha)
print(f"Sua senha gerada é: {senha}")