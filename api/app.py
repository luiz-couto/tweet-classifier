from datetime import datetime
from flask import Flask
from flask import request
import os
import json
import pickle
import requests

PORT = 5021

model_version = os.environ.get('MODEL_VERSION')
app = Flask(__name__)

def predict(text):
    url = "https://raw.github.com/luiz-couto/tweet-classifier/master/models/" + model_version
    req = requests.get(url)
    open(model_version,'wb').write(req.content)

    data = pickle.load(open(model_version, "rb" ))

    clf = data["model"]
    predicted = clf.predict([text])
    return int(predicted[0]), data["model_date"]


@app.route("/api/american", methods = ['POST'])
def isAmerican():
    if (not request.is_json):
        print("missing JSON header")
        return app.response_class(status=400)
    
    print("MODEL_VERSION:", model_version)

    content = request.get_json()
    text = content["text"]

    predicted, date = predict(text)
    
    response = app.response_class(
        response=json.dumps({ 
            "isAmerican": predicted,
            "version": model_version,
            "model_date": datetime.utcfromtimestamp(int(date)).strftime('%Y-%m-%d %H:%M:%S'),

        }),
        status=200,
        mimetype='application/json'
    )

    return response

