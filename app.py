from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
from numpy import array
from lpsolvers import solve_lp
#from sklearn.externals import joblib
#from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

#def scale(payload):
#    """Scales Payload"""
#    
#    LOG.info(f"Scaling Payload: \n{payload}")
#    scaler = StandardScaler().fit(payload.astype(float))
#    scaled_adhoc_predict = scaler.transform(payload.astype(float))
#    return scaled_adhoc_predict

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
        
        input looks like:

        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        
        result looks like:
        { "prediction": [ <val> ] }
        
        """
    
    # Logging the input payload
    json_payload = request.json
    LOG.info(f"JSON payload: \n{json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"Inference payload DataFrame: \n{inference_payload}")
#    # scale the input
#    scaled_payload = scale(inference_payload)
    # get an output prediction from the pretrained model, clf
    #prediction = list(clf.predict(scaled_payload))
    results  = list(1,2,3)
    # TO DO:  Log the output prediction value
    LOG.info(f"Prediction: {prediction}")
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # load pretrained model as clf
#    clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80


#c = array([1., 2., 3.])
#G = array([[1., 2., -1.], [2., 0., 1.], [1., 2., 1.], [-1., -1., -1.]])
#h = array([4., 1., 3., 2.])

#print("LP solution:", solve_lp(c, G, h))

