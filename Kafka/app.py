from flask import Flask, render_template, Response
from pykafka import KafkaClient


def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to home page"


# Consumer API
@app.route('/topic/<topic_name>')
def get_messages(topic_name):
    client = get_kafka_client()

    def events():
        for i in client.topics[topic_name].get_simple_consumer():
            yield 'data:{0}\n\n'.format(i.value.decode())

    return Response(events(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
