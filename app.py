from flask import Flask, request
import jsonify

app = Flask(__name__)

@app.route('/word', methods=['POST'])
def word():
  pass()
  
  
 if __name__ == '__main__':
  app.run(debug=True)
