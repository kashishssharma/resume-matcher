from sklearn.feature_extraction.text import TfidfVectorizer
from core.constants import GENERIC_KEYWORDS

def extract_keywords(text: str, top_n: int = 20) -> list:
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([text])

    scores = tfidf_matrix.toarray()[0]
    keywords = vectorizer.get_feature_names_out()

    scored = list(zip(keywords, scores))
    scored.sort(key=lambda x: x[1], reverse=True)

    filtered = [
        word for word, _ in scored
        if word not in GENERIC_KEYWORDS
    ]

    return filtered[:top_n]
