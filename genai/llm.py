import requests
from config import OPENAI_API_KEY

OPENAI_URL = "https://api.openai.com/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

def ask_llm(prompt: str) -> str:
    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a legal assistant for Indian SMEs. Explain contracts clearly."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(OPENAI_URL, headers=HEADERS, json=payload, timeout=60)

    if response.status_code != 200:
        raise RuntimeError(f"OpenAI API error: {response.text}")

    data = response.json()
    return data["choices"][0]["message"]["content"]
