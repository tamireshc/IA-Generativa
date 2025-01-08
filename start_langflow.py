from langflow.load import run_flow_from_json

TWEAKS = {
    "ChatInput-ZJOlj": {
        "background_color": "",
        "chat_icon": "",
        "files": "",
        "input_value": "Hello",
        "sender": "User",
        "sender_name": "User",
        "session_id": "",
        "should_store_message": True,
        "text_color": "",
    },
    "Prompt-2Ak99": {
        "template": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh."
    },
    "ChatOutput-KkHqn": {
        "background_color": "",
        "chat_icon": "",
        "data_template": "{text}",
        "input_value": "",
        "sender": "Machine",
        "sender_name": "AI",
        "session_id": "",
        "should_store_message": True,
        "text_color": "",
    },
    "GoogleGenerativeAIModel-x3xmt": {
        "google_api_key": "AIzaSyCq3PaYu582eYGZ02j0TeaPwY3cvE5Dvg0",
        "input_value": "",
        "max_output_tokens": None,
        "model": "gemini-1.5-flash",
        "n": None,
        "stream": False,
        "system_message": "",
        "temperature": 0.1,
        "top_k": None,
        "top_p": None,
    },
}

result = run_flow_from_json(
    input_value="Ola meu nome é tamires",
    flow="Basic Prompting.json",
    session_id="",  # provide a session id if you want to use session state
    fallback_to_env_vars=True,  # False by default
    tweaks=TWEAKS,
)

print(result)
