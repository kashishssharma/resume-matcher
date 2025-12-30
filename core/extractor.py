from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text: str, top_n: int = 20) -> list:
    """
    Extract top N keywords using TF-IDF.
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([text])

    scores = tfidf_matrix.toarray()[0]
    keywords = vectorizer.get_feature_names_out()

    scored_keywords = list(zip(keywords, scores))
    scored_keywords.sort(key=lambda x: x[1], reverse=True)

    return [word for word, score in scored_keywords[:top_n]]

