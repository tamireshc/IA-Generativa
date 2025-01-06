import google.generativeai as genai
import os
import PyPDF2

genai.configure(api_key=os.environ["GEMINI_API_KEY"])  # Configure a chave de API

model = genai.GenerativeModel("gemini-1.5-flash")  # Escolha o modelo


def extrair_texto_pdf(path):
    texto = ""
    with open(path, "rb") as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        for pagina in range(len(leitor_pdf.pages)):
            pagina_obj = leitor_pdf.pages[pagina]
            texto += pagina_obj.extract_text()
    return texto


texto = extrair_texto_pdf("./artigo.pdf")

prompt = f"Resuma este texto {texto}"  # Defina o prompt


response = model.generate_content(prompt)  # Gere o conteúdo

print(response.text)
