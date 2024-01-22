from preprocessing.language import unite_by_stemming
from preprocessing.statistical import remove_most_frequent_terms
from preprocessing.tokenizer import (
    normalize_tokens,
    tokenize_text,
)


def preprocess_document(document):
    """produce a list of preprocessed and ordered token out of document"""
    tokens = tokenize_text(document)
    tokens = normalize_tokens(tokens)
    tokens = unite_by_stemming(tokens)
    return tokens


def preprocess_document_collection(dataset):
    """produces a map of documents and their list of preprocessed and ordered tokens"""
    preprocessed_documents = {}
    for news_id, document in dataset.items():
        preprocessed_documents[news_id] = preprocess_document(document["content"])

    preprocessed_documents = remove_most_frequent_terms(preprocessed_documents, 50)

    return preprocessed_documents
