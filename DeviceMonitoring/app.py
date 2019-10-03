import uuid

from flask import Flask, jsonify, request, json
from elasticsearch import Elasticsearch
from kafka import KafkaProducer


es = Elasticsearch()


app = Flask(__name__)


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))


@app.route("/postElastic", methods=['POST'])
def post_elastic():
    message = request.get_json()
    producer.send('newTopic', value=message)
    producer.flush()
    print(message)
    return message


if __name__ == '__main__':
    app.run(debug=True)
