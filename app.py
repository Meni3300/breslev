from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('breslev_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

@app.route('/articles', methods=['GET'])
def get_articles():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
