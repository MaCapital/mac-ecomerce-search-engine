import json
from flask import Flask, jsonify, request
from inMemoryInvItems import generate_reverse_indexing, getItems
from searchService import searchByText

app = Flask(__name__)

#app.run(debug=True)

@app.route('/search')
def search():
    args = request.args
    text = args.get("text")
    print(text)
    return jsonify(searchByText(text))

@app.route('/nn')
def hello():
    return jsonify(getItems())

