import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializa o cliente OpenAI
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN"),
)

def ler_arquivo(caminho):
    """Lê o conteúdo de um arquivo de texto."""
    with open(caminho, "r", encoding="utf-8") as file:
        return file.read()

def classificar_mensagem(mensagem):
    """Classifica a mensagem usando o modelo de IA."""
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente de monitoramento de pais para conversas de crianças ou adolescentes "
                    "sobre suspeita de assédio de um adulto online, que se passa por criança. Você analise a conversa e diz se tem assédio ou não. "
                    "Se sim, classifique como assédio e se não, classifique como não assédio."
                ),
            },
            {
                "role": "user",
                "content": mensagem
            },
        ],
        model=os.getenv("GITHUB_MODEL", "gpt-4o"),
    )
    return response.choices[0].message.content

def main():
    # Obtém o diretório do script atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Caminhos dos arquivos
    arquivos = ["mensagem_assedio.txt", "mensagem_assedio2.txt"]

    # Processa cada arquivo
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(diretorio_atual, arquivo)
        mensagem = ler_arquivo(caminho_arquivo)
        classificacao = classificar_mensagem(mensagem)
        print(f"Classificação para {arquivo}: {classificacao}")

if __name__ == "__main__":
    main()
