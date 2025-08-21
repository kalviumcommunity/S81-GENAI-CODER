import config
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=config.GOOGLE_API_KEY)

# Load model with generation configs
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config={
        "temperature": 0.9,
        "top_p": 0.9
    }
)

# One-shot system prompt for ProDev AI
SYSTEM_PROMPT = """
You are ProDev AI — a professional full-stack coding assistant.
- Always return complete, runnable code.
- Use clean coding practices with comments.
- Provide a short explanation in markdown after the code.
"""

def ask_model(prompt):
    # Combine system + user request
    response = model.generate_content(SYSTEM_PROMPT + "\n\nUser Request: " + prompt)

    print("\nProDev AI Response:\n", response.text)

    if hasattr(response, "usage_metadata"):
        tokens_in = response.usage_metadata.prompt_token_count
        tokens_out = response.usage_metadata.candidates_token_count
        total = response.usage_metadata.total_token_count
        print(f"\nToken Usage: Input={tokens_in}, Output={tokens_out}, Total={total}\n")
    else:
        print("\nToken usage metadata not available in this SDK.\n")

    return response

# Example query
ask_model("Build a simple React counter app with increment and decrement buttons.")
