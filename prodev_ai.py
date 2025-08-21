import config
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=config.GOOGLE_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# ProDev AI user prompt
user_prompt = """
You are ProDev AI, a professional full-stack coding assistant.

Task: Write a complete, runnable program in Python that fetches weather data from a free API
and prints today's temperature in Celsius for a given city.

Think step by step:
1. Choose a reliable free API (like OpenWeatherMap).
2. Show how to make an HTTP request in Python.
3. Parse the response JSON to extract temperature data.
4. Handle possible errors (invalid API key, bad city name, etc).
5. Print today's temperature in a clear format.

Finally, present the output strictly in this JSON structure:
{
  "code": "... full Python code here ...",
  "explanation": "... short explanation of how it works ..."
}
"""

# Start chat
chat = model.start_chat()
response = chat.send_message(user_prompt)

# Print model response
print(response.text)
