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


@app.route("/postData2", methods=['POST'])
def post_data2():
    # id = request.form['id']
    # status = request.form['status']
    # strength = request.form['strength']

    uid = uuid.uuid1()

    id = uid
    status = "good : "+str(uid)
    strength = "strong : "+str(uid)

    body = {
        'id': id,
        'status': status,
        'strength': strength
    }

    result = es.index(index='status', doc_type='device', id=id, body=body)
    return jsonify(result)


app.run(port=5000, debug=True)
