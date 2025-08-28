import config
import google.generativeai as genai
import json
import pinecone
import uuid

# ------------------------
# Configure APIs
# ------------------------
genai.configure(api_key=config.GOOGLE_API_KEY)

# Initialize Pinecone
pinecone.init(api_key=config.PINECONE_API_KEY, environment=config.PINECONE_ENV)
INDEX_NAME = "prodev-code"

# Create index if not exists
if INDEX_NAME not in pinecone.list_indexes():
    pinecone.create_index(INDEX_NAME, dimension=1536)  # adjust dimension for embedding model
index = pinecone.Index(INDEX_NAME)

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# ------------------------
# System prompt
# ------------------------
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

# ------------------------
# Functions
# ------------------------
def process_code_response(response_text):
    """Parse JSON from AI response"""
    try:
        data = json.loads(response_text)
        code = data.get("code", "")
        explanation = data.get("explanation", "")
        return code, explanation
    except Exception as e:
        print("⚠️ Failed to parse JSON:", e)
        return response_text, "No structured explanation returned."

def ask_model(user_prompt):
    """Generate code + explanation, create embeddings, and store in vector DB"""
    full_prompt = SYSTEM_PROMPT + "\n\nUser Request:\n" + user_prompt
    response = model.generate_content(full_prompt)

    # Parse JSON
    code, explanation = process_code_response(response.text)
    print("\n🟢 Code:\n", code)
    print("\n📝 Explanation:\n", explanation)

    # Generate embeddings
    embedding_text = code + "\n\n" + explanation
    try:
        embedding_response = genai.embeddings.create(
            model="textembedding-gecko-001",
            text=embedding_text
        )
        embedding_vector = embedding_response.data[0].embedding
    except Exception:
        print("⚠️ Embeddings not available, using zero vector fallback.")
        embedding_vector = [0.0] * 1536

    # Store in Pinecone
    vector_id = str(uuid.uuid4())
    metadata = {
        "prompt": user_prompt,
        "code": code,
        "explanation": explanation
    }
    index.upsert([(vector_id, embedding_vector, metadata)])
    print(f"✅ Stored in Pinecone with ID: {vector_id}")

    return {
        "code": code,
        "explanation": explanation,
        "embedding": embedding_vector
    }

def evaluate_prompt(user_prompt):
    """Evaluate a single prompt with basic testing"""
    result = ask_model(user_prompt)

    # Basic test: code is non-empty and contains 'return'
    test_passed = bool(result["code"]) and "return" in result["code"]

    evaluation_result = {
        "prompt": user_prompt,
        "code": result["code"],
        "explanation": result["explanation"],
        "embedding": result["embedding"],
        "test_passed": test_passed
    }

    return evaluation_result

# ------------------------
# Example evaluation dataset
# ------------------------
evaluation_dataset = [
    {"description": "Simple React counter with TailwindCSS", "prompt": "Build a simple React counter app with TailwindCSS."},
    {"description": "React button toggle component", "prompt": "Create a React button toggle component with TailwindCSS."},
    {"description": "React input form validation", "prompt": "Create a React input form with validation using TailwindCSS."}
]

# ------------------------
# Run evaluation and store embeddings
# ------------------------
results = []
for item in evaluation_dataset:
    print(f"\n=== Evaluating: {item['description']} ===")
    eval_result = evaluate_prompt(item["prompt"])
    results.append(eval_result)

print("\n✅ Evaluation Results:")
for r in results:
    print(r)
