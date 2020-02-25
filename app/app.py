from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings', methods=['GET'])
def get_greeting():
 return jsonify(['Hello world!', 'Hello, world?', 'World, Hello!'])
 
if __name__ == "__main__":
    app.run(host="0.0.0.0")