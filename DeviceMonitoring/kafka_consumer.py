import uuid

from elasticsearch import Elasticsearch
from flask import Flask, jsonify
from kafka import KafkaConsumer

es = Elasticsearch()
app = Flask(__name__)


def kafka_consumer():
    consumer = KafkaConsumer('newTopic', bootstrap_servers=['localhost:9092'], auto_offset_reset='latest',
                             enable_auto_commit=True)
    print(consumer)
    for message in consumer:
        message = message.value
        print('consumed: ' + str(message))
        write_to_elasticsearch(message)


def write_to_elasticsearch(kafka_message):
    print('m: ' + str(kafka_message))
    kafka_message = kafka_message.decode("utf-8")
    print(kafka_message)
    id = uuid.uuid1()
    result = es.index(index='status_f', id=id, body=kafka_message)
    print("es_data: " + str(jsonify(result)))
    return jsonify(result)


with app.app_context():
    kafka_consumer()

if __name__ == '__main__':
    app.run(debug=True)
