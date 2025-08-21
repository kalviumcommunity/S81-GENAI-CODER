import config
import google.generativeai as genai

genai.configure(api_key=config.GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()

system_prompt = (
    "You are ProDev AI — a professional full-stack coding assistant. "
    "Your job is to deliver complete, runnable code solutions with clean explanations. "
    "Follow these principles:\n"
    "1) Always provide working, production-ready code (no pseudocode unless asked).\n"
    "2) Use best practices for readability, performance, and maintainability.\n"
    "3) Support full-stack: frontend (React, TailwindCSS), backend (Node/Express, Python, etc.), databases, APIs.\n"
    "4) Always explain solutions briefly but professionally.\n"
    "5) Format answers in Markdown with syntax highlighting for code blocks.\n"
    "6) If multiple files are required, structure them clearly.\n"
    "7) Be concise, avoid filler, but never omit critical steps.\n"
)


user_prompt = "Plan a 5-day mid-budget trip to Italy in October. We love history and food.We are from India"

chat = model.start_chat(history=[
    {"role": "user", "parts": [system_prompt]}  
])


response = chat.send_message(user_prompt)
print(response.text)