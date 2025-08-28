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

# Function to parse AI response
def process_code_response(response_text):
    try:
        data = json.loads(response_text)
        code = data.get("code", "")
        explanation = data.get("explanation", "")
        return code, explanation
    except Exception as e:
        print("⚠️ Failed to parse JSON:", e)
        return response_text, "No structured explanation returned."

# Function to run evaluation on a single prompt
def evaluate_prompt(user_prompt):
    result = ask_model(user_prompt)
    
    # Basic testing framework: check code is non-empty and contains some keywords
    test_passed = bool(result["code"]) and "return" in result["code"]
    
    evaluation_result = {
        "prompt": user_prompt,
        "code": result["code"],
        "explanation": result["explanation"],
        "embedding": result["embedding"],
        "test_passed": test_passed
    }
    
    return evaluation_result

# Wrapper for generating code and embeddings
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

# Example evaluation dataset
evaluation_dataset = [
    {"description": "Simple React counter with TailwindCSS", "prompt": "Build a simple React counter app with TailwindCSS."},
    {"description": "React button toggle component", "prompt": "Create a React button toggle component with TailwindCSS."},
    {"description": "React input form validation", "prompt": "Create a React input form with validation using TailwindCSS."}
]

# Run evaluation
results = []
for item in evaluation_dataset:
    print(f"\n=== Evaluating: {item['description']} ===")
    eval_result = evaluate_prompt(item["prompt"])
    results.append(eval_result)

print("\n✅ Evaluation Results:")
for r in results:
    print(r)
