import streamlit as st
from nlp.parser import parse_document
from nlp.language import normalize_language
from nlp.clause_extraction import extract_clauses
from risk.risk_rules import detect_risks
from risk.risk_scoring import clause_risk_score, contract_risk_score
from genai.explanations import explain_clause
from genai.suggestions import suggest_alternative
from utils.audit import log_action

st.title("📄 SME Legal AI Assistant")

file = st.file_uploader("Upload contract", type=["pdf", "docx", "txt"])

if file:
    path = f"data/uploads/{file.name}"
    with open(path, "wb") as f:
        f.write(file.getbuffer())

    text = parse_document(path)
    clean_text, lang = normalize_language(text)
    st.info(f"Language detected: {lang}")

    clauses = extract_clauses(clean_text)
    scores = []

    for i, clause in enumerate(clauses[:10]):
        risks = detect_risks(clause)
        score = clause_risk_score(risks)
        scores.append(score)

        st.subheader(f"Clause {i+1} | Risk: {score}")
        st.write(explain_clause(clause))

        if score != "Low":
            st.warning("⚠ Risk detected")
            st.info(suggest_alternative(clause))

    st.success(f"Overall Contract Risk: {contract_risk_score(scores)}")
    log_action("user", "contract analyzed")
