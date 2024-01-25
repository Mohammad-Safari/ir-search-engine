from hazm import Stemmer


def unite_by_stemming(tokens: list[str]) -> list[str]:
    """use hazm for uniting term tokens based on their stemming"""
    stemmer = Stemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens
