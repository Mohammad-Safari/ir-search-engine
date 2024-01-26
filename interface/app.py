from flask import Flask, render_template, request
from engine.optimization import create_champion_lists, pivot_tf_idf_weights

from engine.similarity import search_documents, vectorize_query
from interface.configuration import AppConfig

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_query = request.form["query"]
        query_vector = vectorize_query(user_query)
        result_documents = search_documents(query_vector, get_weights(query_vector.keys()))

        result_documents = [AppConfig.collection[i] for i, _ in result_documents[: AppConfig.RESULT_LIMIT]]
        return render_template("index.html", query=user_query, results=result_documents)

    return render_template("index.html", query="", results=[])


def get_weights(query_terms: list[str]):
    if AppConfig.USE_CHAMPION_LIST:
        return create_champion_lists(
            query_terms, AppConfig.pivoted_tf_idf_weights, AppConfig.CHAMPION_SIZE
        )
    else:
        return AppConfig.tf_idf_weights


def start_webui(collection_input, inverted_index_input, tf_idf_weights_input):
    AppConfig.collection = collection_input
    AppConfig.inverted_index = inverted_index_input
    AppConfig.tf_idf_weights = tf_idf_weights_input
    AppConfig.pivoted_tf_idf_weights = pivot_tf_idf_weights(
        inverted_index_input, tf_idf_weights_input
    )
    app.run(debug=True)
