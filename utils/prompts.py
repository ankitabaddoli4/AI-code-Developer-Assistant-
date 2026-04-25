def generate_code_prompt(user_input):
    return f"Write clean and efficient code for: {user_input}"

def bug_detection_prompt(code):
    return f"Find bugs in this code and explain:\n{code}"

def fix_code_prompt(code):
    return f"Fix the bugs in this code and return corrected version:\n{code}"
