import random

def escolher_palavra():
    """Escolhe uma palavra aleatória de uma lista."""
    palavras = ["python", "programacao", "desenvolvimento", "tecnologia", "algoritmo"]
    return random.choice(palavras)

def jogar_forca():
    """Função principal do jogo da forca."""
    print("Bem-vindo ao jogo da forca!")
    palavra = escolher_palavra()
    tentativas = 6
    letras_adivinhadas = []

    # Mostra a palavra oculta com underscores
    palavra_oculta = ["_" for _ in palavra]

    while tentativas > 0 and "_" in palavra_oculta:
        print("\nPalavra:", " ".join(palavra_oculta))
        print(f"Tentativas restantes: {tentativas}")

        # Solicita uma letra ao usuário
        letra = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi usada
        if letra in letras_adivinhadas:
            print("Você já tentou essa letra!")
            continue

        letras_adivinhadas.append(letra)

        # Verifica se a letra está na palavra
        if letra in palavra:
            print("Boa! A letra está na palavra!")
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            print("Ops! A letra não está na palavra.")
            tentativas -= 1

    # Verifica se o jogador ganhou ou perdeu
    if "_" not in palavra_oculta:
        print("\nParabéns! Você adivinhou a palavra:", palavra)
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

# Chama a função principal
jogar_forca()