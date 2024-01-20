from document_preprocess.preprocess import preprocess_document


FREQUENCY_KEY = "freq"


def build_inverted_index(preprocessed_documents):
    inverted_index = {}
    for news_id, doc_tokens in preprocessed_documents.items():
        for token_position in range(len(doc_tokens)):
            token = doc_tokens[token_position]
            if token not in inverted_index:
                inverted_index[token] = {FREQUENCY_KEY: 0}
            if news_id not in inverted_index[token]:
                inverted_index[token][news_id] = []
            inverted_index[token][news_id].append(token_position)
            inverted_index[token][FREQUENCY_KEY] += 1
    return inverted_index


def simple_search(query, inverted_index):
    query_tokens = preprocess_document(query)
    relevant_documents = set()
    for token in query_tokens:
        if token in inverted_index:
            relevant_documents.update(inverted_index[token])
    return relevant_documents
