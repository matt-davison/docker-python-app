from flask import Flask, jsonify, redirect, url_for, request
import time
import uuid

app = Flask(__name__)
'''
    {
    "id": "string",
    "postTime": 0,
    "author": {
      "email": "user@example.com",
      "name": "string"
    },
    "message": "string"
    }
'''
blabs = []

#Add a new Blab
@app.route('/blabs', methods=['POST'])
def newBlab():
    '''
    Payload:
    {
    "author": {
      "email": "user@example.com",
      "name": "string"
    },
    "message": "string"
    }
    
    Response:
    {
    "id": "string",
    "postTime": 0,
    "author": {
      "email": "user@example.com",
      "name": "string"
    },
    "message": "string"
    }
    '''
    content = request.json
    blabs.append({"id": uuid.uuid4(), 
              "postTime": int(time.time()),
              "author": content.get("author"),
              "message": content.get("message")})
    return jsonify(blabs[-1]), 201, {'Content-Type': 'application/json'}

#Get blabs since
@app.route('/blabs', methods=['GET'])
def getBlabs():
    sinceTime = request.args.get("createdSince")
    retBlabs = []
    for blab in blabs:
        if blab.get("postTime") >= int(sinceTime):
            retBlabs.append(blab)
    return jsonify(retBlabs), 200, {'Content-Type': 'application/json'}

#Delete a Blab by id
@app.route('/blabs/<id>', methods=['DELETE'])
def removeBlab(id):
    toDel = str(id)
    for blab in blabs:
        if toDel == str(blab.get("id")):
            print("del match found")
            blabs.remove(blab)
            return "200: Blab deleted successfully", 200
    return "404: Blab not found", 404

'''
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('greetings'))


@app.route('/greetings', methods=['GET'])
def greetings():
    return jsonify(['Hello world!', 'Hello, world?', 'World, Hello!'])
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0")