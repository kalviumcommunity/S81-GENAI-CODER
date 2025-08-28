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

IMPORTANT: Stop generating immediately after the JSON object.
Do not output anything else.
"""

# Function to "call" using structured output
def process_code_response(response_text):
    """
    Simulates function calling: parses the JSON output and returns
    structured data that can be directly used in your program.
    """
    try:
        data = json.loads(response_text)
        code = data.get("code", "")
        explanation = data.get("explanation", "")
        return code, explanation
    except Exception as e:
        print("⚠️ Failed to parse JSON:", e)
        return response_text, "No structured explanation returned."

def ask_model(user_prompt):
    full_prompt = SYSTEM_PROMPT + "\n\nUser Request:\n" + user_prompt
    response = model.generate_content(full_prompt)

    # Function-calling: parse and use the AI response
    code, explanation = process_code_response(response.text)

    print("\n🟢 Code:\n", code)
    print("\n📝 Explanation:\n", explanation)

    # Generate embeddings for the code + explanation
    embedding_text = code + "\n\n" + explanation
    embedding_response = genai.embeddings.create(
        model="textembedding-gecko-001",
        text=embedding_text
    )
    
    embedding_vector = embedding_response.data[0].embedding
    print("\n📌 Embedding Vector Length:", len(embedding_vector))

    return {
        "code": code,
        "explanation": explanation,
        "embedding": embedding_vector
    }

# Example usage
ask_model("Build a simple React counter app with TailwindCSS.")
