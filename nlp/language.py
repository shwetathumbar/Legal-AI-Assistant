from langdetect import detect
from genai.llm import ask_llm

def normalize_language(text: str):
    try:
        language = detect(text)
    except:
        language = "en"

    if language == "hi":
        prompt = f"""
        Translate the following Hindi legal contract text into accurate English.
        Preserve legal meaning. Do not summarize.

        Text:
        {text}
        """
        translated = ask_llm(prompt)
        return translated, "Hindi"

    return text, "English"
