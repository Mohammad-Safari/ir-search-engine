from collections import Counter
from typing import TypeAlias


TermFrequencyList: TypeAlias = list[tuple[str, int]]


def eliminate_most_frequent_terms(
    documents_tokenlist: list[str], most_frequent_terms: list[str]
) -> list[str]:
    """eliminate top frequent tokens of whole document collection"""
    filtered_documents_tokenlist = {}
    for doc_id, tokens in documents_tokenlist.items():
        filtered_tokens = [token for token in tokens if token not in most_frequent_terms]
        filtered_documents_tokenlist[doc_id] = filtered_tokens

    return filtered_documents_tokenlist


def get_most_frequent_terms_with_freq(
        documents_tokenlist: list[str],
          threshold: int) -> TermFrequencyList:
    """ setup a list of most frequent terms in collection with their frequency """
    term_frequencies = None
    for doc_id, tokens in documents_tokenlist.items():
        term_frequencies = calculate_term_frequencies(tokens, term_frequencies)
        
    return [(term, freq) for term, freq in term_frequencies.most_common(threshold)]



def calculate_term_frequencies(
    document_tokens: list[str], term_frequencies: Counter = None
) -> Counter:
    """calculate frequency of tokens"""
    if not term_frequencies:
        term_frequencies = Counter()

    term_frequencies.update(document_tokens)

    return term_frequencies
