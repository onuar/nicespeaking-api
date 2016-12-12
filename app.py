from flask import Flask, jsonify, request
from pymongo import MongoClient
import json
from bson import ObjectId

app = Flask(__name__)

@app.route("/api/add", methods=['POST'])
def add_phrases():
    phrases = get_phrases_coll()
    requestjson = request.json["data"]
    data = {"tr":requestjson["tr"],"en":requestjson["en"]}
    id = phrases.insert_one(data).inserted_id
    print("Object Id: "+str(id))
    return jsonify({"status":"ok"})

@app.route("/api/list", methods=['GET'])
def get_all_phrases():
    phrases = get_phrases_coll()
    result = []
    data = phrases.find()
    for d in data:
        result.append({"tr":d["tr"],"en":d["en"]})
    return jsonify({"status":"ok", "data": result})

def get_phrases_coll():
    client = MongoClient("mongodb://dev:dev@ds119548.mlab.com:19548/nicespeaking")
    db = client.nicespeaking
    phrases = db['nice-phrases']
    return phrases

if __name__ == "__main__":
    app.run()