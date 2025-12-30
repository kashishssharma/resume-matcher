import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def preprocess_text(text: str) -> list:
    """
    Clean and tokenize text.
    Returns a list of meaningful words.
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)

    tokens = text.split()
    tokens = [word for word in tokens if word not in ENGLISH_STOP_WORDS]

    return tokens
