from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.local
my_db = db.newCollection

tasks = [
    {
        'id': 1,
        'title': 'EPL',
        'description': 'Welcome to EPL',
        'location': 'England'
    },
    {
        'id': 2,
        'title': 'LA LIGA',
        'description': 'Welcome to LA LIGA',
        'location': 'Spain'
    }
]


@app.route('/tasks', methods=['GET'])
def get_task():
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def write_task():
    task = [
        {
            'id': 3,
            'title': 'LIGUE 1',
            'description': 'Welcome to LIGUE 1',
            'location': 'France'
        }
    ]
    tas = tasks + task
    my_db.insert_many(tas)
    return jsonify({'Tasks: ': tas})


if __name__ == '__main__':
    app.run(debug=True)
