import config
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=config.GOOGLE_API_KEY)

# Model with custom generation config
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config={
        "temperature": 0.7,   # balanced creativity
        "top_p": 0.9,
    }
)

# ProDev AI one-shot system prompt
system_prompt = (
    "🤖 You are Pro-Dev AI — a professional Full Stack Coding Assistant.\n"
    "Your role is to generate complete, runnable, and optimized code along with concise explanations.\n"
    "Always:\n"
    "1) Deliver production-ready code (React, Node.js, Python, etc.).\n"
    "2) Format code properly using Markdown blocks.\n"
    "3) Provide a short explanation after the code (never overly long).\n"
    "4) Respect the requested tech stack (React, TailwindCSS, Express, etc.).\n\n"

    "Example:\n\n"
    "User Request: Build a simple counter app in React.\n"
    "Response:\n"
    "```jsx\n"
    "import { useState } from 'react';\n\n"
    "function Counter() {\n"
    "  const [count, setCount] = useState(0);\n\n"
    "  return (\n"
    "    <div className=\"p-4\">\n"
    "      <p className=\"text-xl\">Count: {count}</p>\n"
    "      <button onClick={() => setCount(count + 1)} className=\"bg-blue-500 text-white px-4 py-2 rounded\">\n"
    "        Increment\n"
    "      </button>\n"
    "    </div>\n"
    "  );\n"
    "}\n\n"
    "export default Counter;\n"
    "```\n\n"
    "Explanation: This React component uses `useState` to manage a counter and updates it when the button is clicked.\n\n"
    "Follow this exact style for all future requests."
)

def ask_model(user_prompt: str):
    # Combine system + user in one-shot
    full_prompt = system_prompt + "\n\nUser Request: " + user_prompt

    response = model.generate_content(full_prompt)

    print("\n💻 ProDev AI Response:\n", response.text)

    if hasattr(response, "usage_metadata"):
        tokens_in = response.usage_metadata.prompt_token_count
        tokens_out = response.usage_metadata.candidates_token_count
        total = response.usage_metadata.total_token_count
        print(f"\n📊 Token Usage: Input={tokens_in}, Output={tokens_out}, Total={total}\n")
    else:
        print("\n⚠️ Token usage metadata not available in this SDK.\n")

    return response


# Example run
ask_model("Build me a responsive login page with React and TailwindCSS.")
