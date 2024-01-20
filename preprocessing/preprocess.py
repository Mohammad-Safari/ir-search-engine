from preprocessing.tokenizer import (
    normalize_tokens,
    tokenize_text,
)


def preprocess_document(document):
    tokens = tokenize_text(document)
    tokens = normalize_tokens(tokens)
    return tokens


def preprocess_document_collection(dataset):
    # Apply preprocessing to each document
    preprocessed_documents = {}
    for news_id, document in dataset.items():
        preprocessed_documents[news_id] = preprocess_document(document["content"])
    return preprocessed_documents
