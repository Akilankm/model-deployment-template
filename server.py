import numpy as np
from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open(f'artifacts/model.pkl', 'rb'))

@app.route('/welcome',methods=['GET','POST'])
def welcome():
    return jsonify("The server is running")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    predictions = model.predict(list(data.values))
    return jsonify(predictions)
    

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)