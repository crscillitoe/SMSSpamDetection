from flask import Flask
from flask_cors import CORS
from keras.models import load_model

app = Flask(__name__)
CORS(app, support_credentials=True)
model = load_model('/home/christian/git/SMSSpamDetection/api/neural_network.h5')
model._make_predict_function()

import api.api_neural
