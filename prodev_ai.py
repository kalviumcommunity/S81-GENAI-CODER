import config
import google.generativeai as genai

# Configure API key
genai.configure(api_key=config.GOOGLE_API_KEY)

# ProDev AI System Prompt
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

# Create model with system prompt
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# === Example Dynamic Inputs (You can change these anytime) ===
language = "Python"
framework = "FastAPI"
feature = "build a REST API with CRUD operations for a todo app"
extras = ["JWT authentication", "SQLite database", "error handling"]

# Build dynamic coding task
user_prompt = f"""
Write a complete {language} project using {framework}.
The task: {feature}.
Include: {", ".join(extras)}.
Return the code in Markdown with syntax highlighting.
If multiple files are needed, clearly separate them with filenames.
"""

# Start chat
chat = model.start_chat()

# Send message
response = chat.send_message(user_prompt)

# Print output
print(response.text)
