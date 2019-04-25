from flask import Flask
from flask_cors import CORS
from keras.models import load_model
from sklearn.tree import DecisionTreeClassifier
from preprocessing import preprocess_data
from data_loader import load_data
import numpy as np
import features

app = Flask(__name__)
CORS(app, support_credentials=True)
model = load_model('/home/christian/git/SMSSpamDetection/api/neural_network.h5')
model._make_predict_function()


file_path = 'spam.csv'
data = load_data(file_path)
preprocess_data(data)

X_pyth = []
y_pyth = []
for d in data:
    text = d['text']
    entry = (
        features.currency_count(text),
        features.url_count(text),
        features.word_count(text),
        features.longest_numerical_string(text),
        features.average_word_length(text),
        features.num_win_occurences(text),
        features.num_free_occurences(text)
    )

    X_pyth.append(entry)

    if d['category'] == 'spam':
        y_pyth.append(0)
    else:
        y_pyth.append(1)

X = np.array(X_pyth)
y = np.array(y_pyth)


# Randomly shuffle data
p = np.random.permutation(len(y_pyth))
X = X[p]
y = y[p]

# Split into training and testing datasets
X_train = X[0:4000]
y_train = y[0:4000]

decision_tree_model = DecisionTreeClassifier()
decision_tree_model.fit(X_train, y_train)

import api.api_neural
