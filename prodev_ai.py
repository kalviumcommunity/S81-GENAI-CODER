import config
import google.generativeai as genai
import json

# Configure Gemini
genai.configure(api_key=config.GOOGLE_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """
You are Pro-Dev AI — a professional full-stack coding assistant.
- Always return complete, runnable code.
- Provide a short explanation in markdown after the code.
- Follow clean coding practices with comments.

Respond ONLY in JSON with the following structure:
{
  "code": "Complete runnable code as string",
  "explanation": "Short explanation in markdown"
}
"""

def ask_model(user_prompt):
    full_prompt = SYSTEM_PROMPT + "\n\nUser Request:\n" + user_prompt
    response = model.generate_content(full_prompt)

    try:
        # Parse JSON from response
        output = json.loads(response.text)
        code = output.get("code", "")
        explanation = output.get("explanation", "")
    except Exception as e:
        print("⚠️ Failed to parse JSON:", e)
        code = response.text
        explanation = "No structured explanation returned."

    print("\n🟢 Code:\n", code)
    print("\n📝 Explanation:\n", explanation)

    return {"code": code, "explanation": explanation}

# Example usage
ask_model("Build a simple React counter app with TailwindCSS.")
