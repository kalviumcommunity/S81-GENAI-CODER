import config
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=config.GOOGLE_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define system prompt for ProDev AI
system_prompt = (
    "You are ProDev AI, a professional full-stack coding assistant.\n"
    "Your job is to generate complete, runnable code solutions.\n"
    "Always include:\n"
    "1) Code (clean & well-commented)\n"
    "2) A short explanation in Markdown after the code\n"
    "Respond in valid JSON format with keys: {\"code\": \"...\", \"explanation\": \"...\"}\n"
    "Do not include comments outside JSON. Keep it concise but professional."
)

# Example user request
user_prompt = "Build a Python script that fetches weather data from an API and prints today's temperature."

# Start chat with system role
chat = model.start_chat(history=[
    {"role": "user", "parts": [system_prompt]}
])

# Send user query
response = chat.send_message(user_prompt)

# Print output
print(response.text)
