# S81-GENAI-CODER
# 🤖 AI Coder Assistant

AI Coder Assistant is an intelligent coding assistant powered by LLMs (such as OpenAI or Gemini) designed to help developers write, understand, debug, and enhance code across multiple languages.

## 🚀 Features

### ✅ 1. Code Execution
- Run code snippets in various programming languages including Python, JavaScript, C++, Java, and more.
- Uses secure sandboxing to execute user-provided code safely.
- Displays formatted output instantly.

**Example:**  
> User: "Run this Python code and show me the output."

### ✅ 2. Code Error Explanation
- Understand errors in your code using LLM reasoning.
- Provides human-friendly explanations of complex error messages and stack traces.
  
**Example:**  
> User: "Explain this error in my Java code."

### ✅ 3. Function Calling (LLM Tools)
Utilizes function calling capabilities of LLMs to delegate certain tasks to backend functions:
  
| Function | Description |
|---------|-------------|
| `runCode(language, code)` | Executes code in a sandbox |
| `generateTestCases(fnName)` | Generates sample test cases |
| `fetchDocumentation(topic)` | Retrieves official docs and links |

These functions are triggered contextually based on user input.

**Example:**  
> User: "Generate test cases for my function `sumArray`."  
> Assistant calls `generateTestCases("sumArray")`.

### ✅ 4. Retrieval-Augmented Generation (RAG)
- Enhances answers using external sources like:
  - StackOverflow discussions
  - GitHub code samples
  - Official documentation
- Injects retrieved information into the LLM prompt to generate contextually rich responses.


### ✅ 5. Auto Test Case Generation
- Automatically generates meaningful test cases for your functions.
- Helps with edge case testing and validation.

### ✅ 6. Fix My Code
- Paste your broken code and get a corrected version with explanations.
- LLM identifies and fixes syntax or logical bugs intelligently.

**Example:**  


### ✅ 7. Documentation Finder
- Instantly fetch official documentation links for languages, libraries, or frameworks.
- Pulls from MDN, Python Docs, Java Docs, and more.

**Example:**  


---

## 🧠 Powered By

- **LLMs:** OpenAI GPT-4 / Gemini 1.5  
- **Function Calling APIs**  
- **Secure Code Execution Engine**  
- **RAG Pipelines with Web Retrieval**

---


