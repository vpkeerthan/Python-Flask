from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch


es = Elasticsearch()


app = Flask(__name__)


@app.route("/home")
def home():
    return "Welcome to home page"


@app.route("/getData", methods=['GET'])
def get_data():
    results = es.get(index='status', doc_type='device', id='my-new-slug')
    return jsonify(results)


@app.route("/postData", methods=['POST'])
def post_data():
    status = request.form['status']
    strength = request.form['strength']

    body = {
        'status': status,
        'strength': strength
    }

    result = es.index(index='status', doc_type='device', id='new-slug', body=body)
    return jsonify(result)


app.run(port=5000, debug=True)
