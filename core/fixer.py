def fix_code(code):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": code}]
        )
        return response.choices[0].message.content

    except Exception:
        if "for i in range" in code and ":" not in code:
            return code.replace(")", "):")

        return code