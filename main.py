import json
from engine.weighting import calculate_tf_idf_weights
from interface.app import start_webui

from preprocessing.preprocess import preprocess_document_collection
from indexing.indexer import build_inverted_index
from indexing.persistent import ind2json, load_index, save_index

collection_file_name = "IR_data_news_12k.json"
inverted_index_file_name = "IR_data_news_12k.ind"
repetitive_eliminate_rank = 50
reindex_collection = True


def get_index(
    document_collection,
    inverted_index_file_name=inverted_index_file_name,
    reindex_collection=True,
):
    if reindex_collection:
        preprocessed_collection, eliminated_terms_with_freq = preprocess_document_collection(document_collection, repetitive_eliminate_rank)
        export_term_frequency(eliminated_terms_with_freq)
        export_tokens(preprocessed_collection)
        inverted_index = build_inverted_index(preprocessed_collection)
        save_index(inverted_index, f"data/{inverted_index_file_name}")
    else:
        inverted_index = load_index(f"data/{inverted_index_file_name}")
    return inverted_index


def export_term_frequency(term_frequencies):
    with open("data/most_frequent.txt", "w") as file:
        file.write(",".join(str(tuple) for tuple in term_frequencies))


def export_tokens(preprocessed_collection):
    with open("data/tokenized_document.txt", "w") as file:
        count = 0
        for doc in preprocessed_collection.values():
            file.write(f"--------{count}---------")
            file.write(",".join(doc))
            count += 1


def get_collection(collection_file_name):
    with open(f"data/{collection_file_name}", "r", encoding="utf-8") as file:
        document_collection = json.load(file)
    return document_collection


if __name__ == "__main__":
    # read the JSON file
    document_collection = get_collection(collection_file_name)

    # load an Index
    inverted_index = get_index(document_collection, reindex_collection=reindex_collection)

    # persist a human readble inverted index in json format
    ind2json(inverted_index_file_name)

    # calculate tf-if weights
    tf_idf_weights = calculate_tf_idf_weights(inverted_index, len(document_collection))

    start_webui(document_collection, inverted_index, tf_idf_weights)
