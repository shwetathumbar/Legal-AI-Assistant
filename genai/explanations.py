from genai.llm import ask_llm

def explain_clause(clause):
    return ask_llm(
        f"Explain this contract clause in simple business language:\n{clause}"
    )
