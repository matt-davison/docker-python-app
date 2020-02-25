from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greeting', methods=['GET'])
def get_greeting():
 return jsonify(['Hello world!', 'Hello, world?', 'World, Hello!'])

 app.run(host="0.0.0.0")