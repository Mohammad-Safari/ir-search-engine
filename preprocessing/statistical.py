from collections import Counter


def remove_most_frequent_terms(documents_tokenlist, threshold):
    """remove top frequent tokens of whole document collection"""
    term_frequencies = None
    for doc_id, tokens in documents_tokenlist.items():
        term_frequencies = calculate_term_frequencies(tokens, term_frequencies)
    most_frequent_terms = [term for term, _ in term_frequencies.most_common(threshold)]
    print(most_frequent_terms)

    filtered_documents_tokenlist = {}
    for doc_id, tokens in documents_tokenlist.items():
        filtered_tokens = [token for token in tokens if token not in most_frequent_terms]
        filtered_documents_tokenlist[doc_id] = filtered_tokens
    return filtered_documents_tokenlist


def calculate_term_frequencies(document_tokens, term_frequencies=None):
    """calculate frequency of tokens"""
    if not term_frequencies:
        term_frequencies = Counter()

    term_frequencies.update(document_tokens)

    return term_frequencies
