import os
from dotenv import load_dotenv

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
load_dotenv()
client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)
# Obtém o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, "mensagens.txt")
# ler um arquivo de texto com mensagens
with open(caminho_arquivo, "r", encoding="utf-8") as file:
    mensagens = file.read()


response = client.complete(
    messages=[
        SystemMessage(content="Você é um assistente que vai verificar a conversa entre adolescentes sobre cometer suicídio. Classifique assim como alerta sucídio ou não alerta suicídio."),
        UserMessage(content=mensagens),
    ],
    model=os.getenv("GITHUB_MODEL", "gpt-4o"),
)
print(response.choices[0].message.content)
