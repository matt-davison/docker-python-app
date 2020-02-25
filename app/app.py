from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('greetings'))
@app.route('/greetings', methods=['GET'])
def greetings():
 return jsonify(['Hello world!', 'Hello, world?', 'World, Hello!'])
 
if __name__ == "__main__":
    app.run(host="0.0.0.0")