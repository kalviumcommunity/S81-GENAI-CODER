import config
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=config.GOOGLE_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Pro-Dev AI system prompt
SYSTEM_PROMPT = """
You are Pro-Dev AI — a professional full-stack coding assistant.
- Always return complete, runnable code.
- Provide a short explanation in markdown after the code.
- Follow clean coding practices with comments.
"""

def ask_model(user_prompt):
    # Merge system + user prompt
    response = model.generate_content(SYSTEM_PROMPT + "\n\nUser Request:\n" + user_prompt)

    print("\n🤖 Pro-Dev AI Response:\n", response.text)

    # Token usage (if available)
    if hasattr(response, "usage_metadata"):
        tokens_in = response.usage_metadata.prompt_token_count
        tokens_out = response.usage_metadata.candidates_token_count
        total = response.usage_metadata.total_token_count
        print(f"\n🔎 Token Usage: Input={tokens_in}, Output={tokens_out}, Total={total}\n")
    else:
        print("\n Token usage metadata not available in this SDK.\n")

    return response

# Example
ask_model("Build a simple React counter app with TailwindCSS.")
