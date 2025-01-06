# Tradutor de documentos txt em inglês para português

import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])  # Configure a chave de API

model = genai.GenerativeModel("gemini-1.5-flash")  # Escolha o modelo

document = genai.upload_file(path="example.txt")  # Carregue o documento

prompt = "Traduza o texto do arquivo example.txt para o portugues."  # Defina o prompt

response = model.generate_content([document, prompt])  # Gere o conteúdo

try:
    # Abre o arquivo em modo de escrita ('w').
    # Se o arquivo não existir, ele será criado.
    with open("texto_traduzido.txt", "w") as arquivo:
        # Escreve o texto no arquivo
        arquivo.write(response.text)
    print("Texto salvo com sucesso em 'texto_traduzido.txt'")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")
