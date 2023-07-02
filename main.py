from flask import Flask, jsonify, request
from vocabualrio import result
from BinarySearchTree import search_word, BinarySearchTree

app = Flask(__name__)
bst = BinarySearchTree()

for word in result:
    bst.insert(word)


@app.route('/search', methods=['GET'])
def search():
    word = request.args.get('word', '').strip()
    if not word:
        return jsonify(error='No se proporcionó ninguna palabra.')

    found_word = search_word(bst,word)

    return jsonify(result=found_word)


if __name__ == '__main__':
    app.run()