import openai
import os

# Set your OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def ai_review_code(code_snippet):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI code reviewer. Provide suggestions."},
            {"role": "user", "content": f"Review this code:\n{code_snippet}"}
        ]
    )
    return response["choices"][0]["message"]["content"]

# Example: Test AI review on a simple function
code = "def add(a, b): return a+b"
print(ai_review_code(code))
