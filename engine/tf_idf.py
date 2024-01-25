from collections import defaultdict
import math
from typing import TypeAlias

from indexing.indexer import InvertedIndex


TfIdfPseudoVector: TypeAlias = dict[str, float]
DocumentTermFrequency: TypeAlias = dict[str, int]
InvertDocumentFrquency: TypeAlias = dict[str, float]


def calculate_tf_idf_weights(
    inverted_index: InvertedIndex, collection_size: int
) -> dict[str, TfIdfPseudoVector]:
    """Calculate tf-idf weights for each document"""
    tf = calculate_documents_tf(inverted_index)
    idf = calculate_terms_idf(collection_size, inverted_index)

    tf_idf_weights = {
        doc_id: {
            token: (1 + math.log(tf_value)) * idf[token]
            for token, tf_value in tf_values.items()
        }
        for doc_id, tf_values in tf.items()
    }

    return tf_idf_weights


def calculate_terms_idf(
    collection_size: int, inverted_index: InvertedIndex
) -> InvertDocumentFrquency:
    """Calculate inverse document frequency (idf) for each term"""
    idf = {}
    for term, posting in inverted_index.items():
        doc_freq = len(posting)
        idf[term] = math.log(collection_size / doc_freq)
    return idf


def calculate_documents_tf(
    inverted_index: InvertedIndex,
) -> dict[str, DocumentTermFrequency]:
    """Calculate term frequency (tf) for each document"""
    tf = {}
    for term, posting in inverted_index.items():
        docs_id = posting.keys()
        for doc_id in docs_id:
            tf.setdefault(doc_id, defaultdict(int))
            tf[doc_id][term] += 1
    return tf
