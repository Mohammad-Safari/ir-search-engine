from flask import Flask, render_template, request

from engine.similarity import search_documents, vectorize_query

app = Flask(__name__)

collection = {}
tf_idf_weights = {}
inverted_index = {}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_query = request.form["query"]
        query_vector = vectorize_query(user_query)
        result_documents = search_documents(query_vector, tf_idf_weights)

        # Display top 20 relevant documents
        result_documents = [collection[i] for i, _ in result_documents[:20]]
        return render_template("index.html", query=user_query, results=result_documents)

    return render_template("index.html", query="", results=[])


def start_webui(collection_input, inverted_index_input, tf_idf_weights_input):
    global collection
    global tf_idf_weights
    global inverted_index
    collection = collection_input
    tf_idf_weights = tf_idf_weights_input
    inverted_index = inverted_index_input
    app.run(debug=True)
