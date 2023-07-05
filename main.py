from flask import Flask, jsonify, request
from vocabualrio import orden
from BinarySearchTree import search_word, create_binary_search_tree

app = Flask(__name__)
bst = create_binary_search_tree(orden, 0, len(orden) - 1)


@app.route('/search', methods=['GET'])
def search():
    word = request.args.get('word', '').strip()

    found_word = search_word(bst, word)

    return jsonify(result=found_word)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

