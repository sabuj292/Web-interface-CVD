from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from collections.abc import Mapping
# from requests import request

# app= Flask(__name__, template_folder='Template')

app= Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

""" @app.route("/")
def hello():
   return render_template("index.html")
   """


@app.route('/predict', methods=['POST'])
def predict():
    
    data1 = request.form['age']
    data2 = request.form['male']
    data3 = request.form['cigsPerDay']
    data4 = request.form['totChol']
    data5 = request.form['sysBP']
    data6 = request.form['glucose']

    data7 = request.form['diaBP']
    data8 = request.form['prevalentHyp']
    
    data9 = request.form['BPMeds']
    data10 = request.form['diabetes']

   
    data1 = int(data1)
    data2 = int(data2)
    data3 = int(data3)
    data4 = int(data4)
    data5 = int(data5)
    data6 = int(data6)
    data7 = int(data7)
    data8 = int(data8)
    data9 = int(data9)
    data10 = int(data10)

    arr = np.array([[data1, data2, data3, data4, data5, data6]])

    pred = model.predict(arr)

    if pred==1:
        return render_template("index.html", prediction_text="Have higher risk of Cardiovascular Disease")
    else:
        return render_template("index.html", prediction_text="Have lower risk of Cardiovascular Disease")

 

if __name__ == "__main__":
    app.run(debug=True)