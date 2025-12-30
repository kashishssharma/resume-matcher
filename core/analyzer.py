from core.preprocess import preprocess_text
from core.extractor import extract_keywords
from core.similarity import compute_similarity

def analyze_resume(resume_text: str, jd_text: str) -> dict:
    """
    Full analysis pipeline.
    """
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    similarity_result = compute_similarity(resume_keywords, jd_keywords)

    suggestions = []
    if similarity_result["missing_keywords"]:
        suggestions.append(
            "Add missing keywords to skills or project descriptions."
        )

    return {
        "match_score": similarity_result["match_score"],
        "matching_keywords": similarity_result["matching_keywords"],
        "missing_keywords": similarity_result["missing_keywords"],
        "suggestions": suggestions,
    }
