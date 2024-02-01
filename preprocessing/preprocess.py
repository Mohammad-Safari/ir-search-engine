from typing import TypeAlias
from preprocessing.language import unite_by_stemming
from preprocessing.statistical import TermFrequencyList, eliminate_most_frequent_terms, get_most_frequent_terms_with_freq
from preprocessing.tokenizer import (
    normalize_tokens,
    tokenize_text,
)

PreprocessedDocument: TypeAlias = list[str]
PreprocessedCollection: TypeAlias = dict[str, PreprocessedDocument]


def preprocess_document(document: str) -> PreprocessedDocument:
    """produce a list of preprocessed and ordered token out of document"""
    tokens = tokenize_text(document)
    tokens = normalize_tokens(tokens)
    tokens = unite_by_stemming(tokens)
    return tokens

def preprocess_document_collection_parallel(news_id, document):
    r = news_id, preprocess_document(document["content"])
    progress.count()
    return r


def preprocess_document_collection(
    dataset: dict[str, str], repetitive_eliminate_rank: int = 50
) -> tuple[PreprocessedCollection, TermFrequencyList] :
    """produces a map of documents and their list of preprocessed and ordered tokens
    besides eliminated tokens and their frequency"""
    preprocessed_documents = {}
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(preprocess_document_collection_parallel , dataset.keys(), dataset.values()))
    for news_id, preprocessed_document in results:
        preprocessed_documents[news_id] = preprocessed_document[:-2]
    # single thread 
    # for news_id, document in dataset.items():
    #     preprocessed_documents[news_id] = preprocess_document(document["content"])

    most_frequent_terms_with_freq = get_most_frequent_terms_with_freq(preprocessed_documents, repetitive_eliminate_rank)

    filtered_preprocessed_docs = eliminate_most_frequent_terms(preprocessed_documents, list(map(lambda tf: tf[0], most_frequent_terms_with_freq)))

    return filtered_preprocessed_docs, most_frequent_terms_with_freq
