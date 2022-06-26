from flask import Flask
from flask import request
import os
import json
import pickle
import joblib
import requests
import io

PORT = 5021

model_version = "v0.0.2"


url = "https://raw.githubusercontent.com/luiz-couto/tweet-classifier/master/models" + model_version
req = requests.get(url)
open(model_version,'wb').write(req.content)

clf = pickle.load(open(model_version, "rb" ))
predicted = clf.predict(["text"])