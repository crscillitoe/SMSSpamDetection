import features
from data_loader import load_data
from preprocessing import preprocess_data
import matplotlib

from api import app
from api import model
from flask import jsonify
from flask import abort
from flask import request
from flask_cors import cross_origin
import keras

# fixes error on mac
matplotlib.use('TkAgg') 

import numpy as np

@app.route('/api/isSpam', methods=['POST'])
@cross_origin(supports_credentials=True)
def is_spam():
    try:
        text = request.json["Text"]
    except:
        abort(500, 'Text not found')

    X = []
    entry = (
        features.currency_count(text),
        features.url_count(text),
        features.word_count(text),
        features.longest_numerical_string(text),
        features.average_word_length(text),
        features.num_win_occurences(text),
        features.num_free_occurences(text)
    )

    X.append(entry)
    X = np.array(X)

    prediction = model.predict(X)
    print(prediction)
    if (prediction[0])[0] > 0.8:
        return jsonify({"prediction": "Spam", "certainty": "{}".format((prediction[0])[0])})

    return jsonify({"prediction": "Not Spam", "certainty": "{}".format((prediction[0])[1])})

if __name__ == '__main__':
    main()
