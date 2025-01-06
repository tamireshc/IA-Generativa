import google.generativeai as genai
import gradio as gr
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

initial_prompt = "Você é um Assistente de Receitas Culinárias, voce deve encontrar e seguir receitas culinárias, sendo capaz de fornecer receitas baseadas em ingredientes fornecidos, dar dicas de culinária e responder a perguntas relacionadas à preparação de pratos"

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initial_prompt)

chat = model.start_chat()


def gradio_wrapper(message, _history):
    prompt = message
    response = chat.send_message(prompt)
    return response.text


# Crie e lance a interface do chat com o Gradio
chat_interface = gr.ChatInterface(
    fn=gradio_wrapper,
    title="Chatbot Assistente de Receitas Culinárias 🍳",
)
# Inicie a interface
chat_interface.launch()
