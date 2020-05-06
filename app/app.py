from flask import Flask, jsonify, redirect, url_for, request
import time
import uuid
import pymongo
from prometheus_flask_exporter import PrometheusMetrics
import os

mongoClient = pymongo.MongoClient("mongodb://mongo:27017")
mongoCollection = mongoClient["cs2304"]["blabber"]

db_secret = os.getenv('MONGO_SECRET')
if os.getenv('MONGO_CONFIGURED') == 'true' and db_secret is not None:
    print("using secret-provided mongo config")
    mongoClient = pymongo.MongoClient("mongodb://mongo:27017")
    mongoCollection = mongoClient["cs2304"]["blabber"]
    

app = Flask(__name__)

metrics = PrometheusMetrics(app)

#Add a new Blab
@app.route('/blabs', methods=['POST'])
@metrics.counter('blabs_created', 'Number of Blabs created')
def newBlab():
    content = request.json
    newBlab = {"id": str(uuid.uuid4()), 
              "postTime": int(time.time()),
              "author": content.get("author"),
              "message": content.get("message")}
    mongoCollection.insert_one(newBlab)
    newBlab.pop("_id")
    return jsonify(newBlab), 201, {'Content-Type': 'application/json'}

#Get blabs since
@app.route('/blabs', methods=['GET'])
def getBlabs():
    sinceTime = request.args.get("createdSince")
    retBlabs = []
    for item in mongoCollection.find():
        blab = item.copy()
        if blab.get("postTime") >= int(sinceTime):
            blab.pop("_id")
            retBlabs.append(blab)
    return jsonify(retBlabs), 200, {'Content-Type': 'application/json'}

#Delete a Blab by id
@app.route('/blabs/<id>', methods=['DELETE'])
def removeBlab(id):
    result = mongoCollection.delete_one({"id": id})
    if result.deleted_count > 0:
        return "200: Blab deleted successfully", 200
    msg = "404: Blab not found: "+str(id)
    return msg, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")