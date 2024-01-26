import heapq
from math import sqrt
from engine.weighting import TfIdfPseudoVector, calculate_documents_tf
from indexing.indexer import build_inverted_index
from preprocessing.preprocess import preprocess_document


def vectorize_query(query: str) -> TfIdfPseudoVector:
    """actually just a tf psuedo vector"""
    preprocessed_query = preprocess_document(query)
    dummy_index = build_inverted_index({"#": preprocessed_query})
    query_tf = calculate_documents_tf(dummy_index)["#"]
    return query_tf


def search_documents(
    query_vector: dict[str, float],
    document_vectors: dict[str, TfIdfPseudoVector],
    result_limit: int = None,
) -> list[tuple[str, float]]:
    similarities = {}
    for doc_id, doc_vector in document_vectors.items():
        similarity = _calculate_cosine_similarity(query_vector, doc_vector)
        similarities[doc_id] = similarity
    sorted_documents = (
        sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        if not result_limit
        else heapq.nlargest(result_limit, similarities.items(), key=lambda x: x[1])
    )
    return sorted_documents


""" utilities """


def _calculate_dot_product(
    pvector1: dict[str, float], pvector2: dict[str, float]
) -> float:
    dot_product = 0
    for key in pvector1:
        if key in pvector2:
            dot_product += pvector1[key] * pvector2[key]
    return dot_product


def _calculate_norm(pvector: dict[str, float]) -> float:
    norm = sqrt(sum(val**2 for val in pvector.values()))
    return norm


def _calculate_cosine_similarity(
    query_vector: dict[str, float], document_vector: dict[str, float]
):
    dot_product = _calculate_dot_product(query_vector, document_vector)
    # only doc normal wil be calculated and used in formulation
    doc_norm = _calculate_norm(document_vector)
    cosine_similarity = dot_product / doc_norm
    return cosine_similarity
