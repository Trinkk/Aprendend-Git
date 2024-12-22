# Primeiro, certifique-se de instalar o TextBlob:
# pip install textblob

from textblob import TextBlob

def analisar_sentimento(texto):
    """
    Analisa o sentimento de um texto e retorna se é positivo, negativo ou neutro.
    
    Parâmetros:
    texto (str): O texto a ser analisado.
    
    Retorno:
    str: O sentimento do texto (Positivo, Negativo ou Neutro).
    """
    try:
        # Cria um objeto TextBlob com o texto
        analise = TextBlob(texto)

        # Verifica a polaridade do texto
        if analise.sentiment.polarity > 0:
            return "Positivo 😊"
        elif analise.sentiment.polarity < 0:
            return "Negativo 😢"
        else:
            return "Neutro 😐"
    except Exception as e:
        return f"Erro ao analisar o sentimento: {str(e)}"

def main():
    """
    Função principal para solicitar um texto ao usuário e exibir o sentimento analisado.
    """
    print("Bem-vindo ao analisador de sentimentos!")
    texto_usuario = input("Digite um texto para análise de sentimento: ").strip()

    # Verifica se o texto é vazio
    if not texto_usuario:
        print("Erro: O texto não pode estar vazio!")
        return

    # Analisa o sentimento do texto e exibe o resultado
    resultado = analisar_sentimento(texto_usuario)
    print(f"O sentimento do texto é: {resultado}")

# Executa o programa principal
if __name__ == "__main__":
    main()