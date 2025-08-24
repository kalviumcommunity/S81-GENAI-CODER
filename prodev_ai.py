import config
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=config.GOOGLE_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# ProDev AI generic concept prompt
user_prompt = """
You are ProDev AI, a professional full-stack coding assistant.

Task: Write a complete, runnable program in Python based on the given topic.

Steps you must always follow:
1. Choose appropriate libraries or APIs required.
2. Show how to implement the program step by step.
3. Parse/process the response or data correctly.
4. Handle possible errors gracefully.
5. Print or return the result in a clear format.

Finally, always present the output strictly in this JSON structure:
{
  "code": "... full Python code here ...",
  "explanation": "... short explanation of how it works ..."
}

Example topic: Fetch weather data from a free API and print today's temperature in Celsius.
"""

# Start chat
chat = model.start_chat()
response = chat.send_message(user_prompt)

# Print model response
print(response.text)
