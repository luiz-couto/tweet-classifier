from flask import Flask
from flask import request
import json
import pickle

app = Flask(__name__)

@app.route("/api/american", methods = ['POST'])
def isAmerican():
    if (not request.is_json):
        print("missing JSON header")
        return app.response_class(status=400)
    

    content = request.get_json()
    text = content["text"]
    response = app.response_class(
        response=json.dumps({ "isAmerican": text }),
        status=200,
        mimetype='application/json'
    )

    return response

app.run(host='0.0.0.0', port=8090)
