from config import HIGH_RISK_KEYWORDS

def detect_risks(clause_text):
    return [
        kw for kw in HIGH_RISK_KEYWORDS
        if kw.lower() in clause_text.lower()
    ]