def clause_risk_score(risks):
    if len(risks) >= 2:
        return "High"
    elif len(risks) == 1:
        return "Medium"
    return "Low"

def contract_risk_score(scores):
    if "High" in scores:
        return "High"
    elif "Medium" in scores:
        return "Medium"
    return "Low"
