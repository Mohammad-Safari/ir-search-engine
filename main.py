import json

from document_preprocess.preprocess import preprocess_document_collection


# Read the JSON file
with open(f'data/{"IR_data_news_12k.json"}', 'r', encoding='utf-8') as file:
    document_collection = json.load(file)

preprocessed_document_collection = preprocess_document_collection(document_collection)

print(preprocessed_document_collection)