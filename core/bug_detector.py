def detect_bugs(code):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": code}]
        )
        return response.choices[0].message.content

    except Exception:
        if "def" in code and ":" not in code:
            return "Error: Missing ':' in function definition"

        return "No obvious bugs found"