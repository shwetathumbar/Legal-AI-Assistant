from genai.llm import ask_llm

def suggest_alternative(clause):
    return ask_llm(
        f"Suggest a safer SME-friendly alternative clause:\n{clause}"
    )
