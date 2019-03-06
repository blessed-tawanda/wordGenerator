from flask import Flask, request, jsonify
from wordGenerator import WordGenerator

app = Flask(__name__)

@app.route('/word', methods=['POST'])
def word():
  body = request.get_json()
  wordGen = WordGenerator(body['letters'],body['numberOfLettersInWord'])
  return jsonify(wordGen.foundWords)
  
  
if __name__ == '__main__':
  app.run(debug=True, port=2020)
