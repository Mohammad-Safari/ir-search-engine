from collections import defaultdict
from typing import TypeAlias
import heapq

from engine.weighting import TfIdfPseudoVector
from indexing.indexer import InvertedIndex

TfIdfPivotPseudoVector: TypeAlias = dict[str, TfIdfPseudoVector]


def pivot_tf_idf_weights(
    inverted_index: InvertedIndex, tf_idf_weights: dict[str, TfIdfPseudoVector]
) -> TfIdfPivotPseudoVector:
    """pivot tf-idf weights from per document to per term"""
    return {
        term: {
            doc: tf_idf_weights[doc][term]
            for doc in postings
            if isinstance(postings[doc], list)
        }
        for term, postings in inverted_index.items()
    }


def create_champion_lists(
    query_terms: list[str],
    tf_idf_weights: dict[str, TfIdfPseudoVector],
    pivoted_tf_idf_weights: dict[str, TfIdfPivotPseudoVector],
    k=5,
) -> dict[str, TfIdfPseudoVector]:
    """create champion lists for each term based on term-based tf-idf weights"""
    champions_weights = defaultdict(TfIdfPseudoVector)
    for term in query_terms:
        doc_weights = pivoted_tf_idf_weights[term]
        top_doc = heapq.nlargest(k, doc_weights.items(), key=lambda x: x[1]/len(tf_idf_weights[x[0]]))
        for doc_id, doc_weight in top_doc:
            champions_weights[doc_id][term] = doc_weight

    return champions_weights


def prune_documents_weights(
    query_vector: dict[str, float],
    term_vectors: dict[str, TfIdfPivotPseudoVector],
) -> dict[str, TfIdfPseudoVector]:
    """in case of small queries can eliminate a lot of nonrelevant docs,
    participating in similarity calculations by just focusing on query terms"""
    pruned_document_vectors = defaultdict(TfIdfPseudoVector)
    for term in query_vector.keys():
        term_vector = term_vectors[term]
        for doc_id in term_vector.keys():
            pruned_document_vectors[doc_id][term] = term_vectors[term][doc_id]
    return pruned_document_vectors
