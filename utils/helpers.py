import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def validate_input(user_input):
    """
    Check if input is valid
    """
    if not user_input or user_input.strip() == "":
        return False
    return True


def detect_language(code):
    """
    Simple language detection for syntax highlighting
    """
    if not code:
        return "plaintext"

    code = code.lower()

    if "def " in code or "print(" in code:
        return "python"
    elif "public static void main" in code:
        return "java"
    elif "#include" in code:
        return "cpp"
    elif "<html" in code:
        return "html"
    else:
        return "plaintext"