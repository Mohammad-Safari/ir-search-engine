import json

from preprocessing.preprocess import preprocess_document_collection
from indexing.indexer import build_inverted_index
from indexing.persistent import ind2json, load_index, save_index

collection_file_name = "IR_data_news_12k.json"
inverted_index_file_name = "IR_data_news_12k.ind"
reindex_collection = True

# Read the JSON file
with open(f"data/{collection_file_name}", "r", encoding="utf-8") as file:
    document_collection = json.load(file)
# Load an Index
if reindex_collection:
    preprocessed_document_collection = preprocess_document_collection(
        document_collection
    )

    # print(preprocessed_document_collection)

    inverted_index = build_inverted_index(preprocessed_document_collection)
    save_index(inverted_index, f"data/{inverted_index_file_name}")
else:
    inverted_index = load_index(f"data/{inverted_index_file_name}")

    # ind2json(inverted_index_file_name)