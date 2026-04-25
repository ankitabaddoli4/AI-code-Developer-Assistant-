from openai import OpenAI
import os
from dotenv import load_dotenv
from utils.prompts import generate_code_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_code(user_input):
    prompt = generate_code_prompt(user_input)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except Exception:
        # 🔥 SMART FALLBACK
        text = user_input.lower()

        if "factorial" in text:
            return """def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)"""

        elif "palindrome" in text:
            return """def is_palindrome(s):
    return s == s[::-1]"""

        elif "prime" in text:
            return """def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True"""

        elif "fibonacci" in text:
            return """def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b"""

        else:
            return f"# Code for: {user_input}\nprint('Feature coming soon')"
