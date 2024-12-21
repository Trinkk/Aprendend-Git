def eh_palindromo(palavra):
    # Remove espaços e converte para minúsculas para comparação precisa
    palavra_limpa = palavra.replace(" ", "").lower()
    # Inverte a palavra limpa
    palavra_invertida = palavra_limpa[::-1]
    # Verifica se a palavra limpa é igual à palavra invertida
    return palavra_limpa == palavra_invertida

# Testa a função
palavra_teste = input("Digite uma palavra ou frase: ")
if eh_palindromo(palavra_teste):
    print(f'"{palavra_teste}" é um palíndromo.')
else:
    print(f'"{palavra_teste}" não é um palíndromo.')