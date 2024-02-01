# News Basic Search Engine

A simple text processing and search engine with a Flask-based web application user interface, developed in Python. The project is structured into four modules: Preprocessing, Indexing, Search Engine, and a Web Interface.

## Data Input Format

The input data for this project should be provided in a JSON format. Each document is represented as an object with the following fields:

- `"title"`: The title of the document.
- `"content"`: The content or body of the document.
- `"tags"`: A list of tags or keywords associated with the document.
- `"date"`: The date and time of the document in the format "MM/DD/YYYY h:mm:ss AM/PM".
- `"url"`: The URL or source link of the document.
- `"category"`: The category or topic to which the document belongs.

## Modules

### 1. Preprocessing

This module handles functions related to token extraction, normalization, stemming, and lemmatization. Key processes include:

- Token extraction using regular expressions to identify patterns such as words, IDs, and numbers.
- Normalization involving lowercase conversion, Persian and Arabic character equivalence, and standardization of word forms.
- Stemming and lemmatization using the "Hazm" library to unify word roots for improved search functionality.

### 2. Indexing

The Indexing module creates a positional index by building a dictionary of words and their occurrences in the document collection. It includes:

- Creating a dictionary of word occurrences with document IDs and positions.
- Maintaining a common key for all words to track the overall occurrence count in the entire document collection.
- The ability to save and load the index to enhance efficiency and avoid repetitive processing.

### 3. Search Engine

The Search Engine module enables users to perform text searches on the indexed documents. Key features include:

- Implementing parallel processing for efficient text document analysis.
- Allowing users to input queries and retrieving relevant documents based on the created index.
- Handling multiple occurrences and variations of words to enhance search accuracy.

### 4. Web Interface (Flask App)

The Web Interface module provides a user-friendly interface for interacting with the search engine using Flask. It includes:

- A web-based interface allowing users to input queries through a browser.
- Displaying search results in a visually appealing format.
- Options for reloading the index or creating a new one based on user preferences.

## Getting Started

To run the project with the Flask web app, follow these steps:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask app by executing the main script.
4. Open a web browser and navigate to the provided URL to interact with the search engine.

## Future Improvements

This project can be extended and improved by enhancing the web interface, implementing user authentication, and integrating additional features to make the search engine more versatile.

Feel free to explore and contribute to the project to make it even more user-friendly and feature-rich. We welcome your suggestions and contributions!

**Note:** This README is provided in English for broader accessibility, but the project itself is implemented in Persian (Farsi).
