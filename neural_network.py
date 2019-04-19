import features
from data_loader import load_data
from preprocessing import preprocess_data
import matplotlib

# fixes error on mac
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Conv2D, BatchNormalization
from keras.utils import to_categorical

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix

def main():
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
            y_pyth.append([1, 0])
        else:
            y_pyth.append([0, 1])

    X = np.array(X_pyth)
    y = np.array(y_pyth)


    # Randomly shuffle data
    p = np.random.permutation(len(y_pyth))
    X = X[p]
    y = y[p]

    # Split into training and testing datasets
    X_train = X[0:4000]
    y_train = y[0:4000]

    X_test = X[4001:5571]
    y_test = y[4001:5571]

    model = get_neural_network(X.shape[1])
    model.fit(X_train, y_train, epochs=100, batch_size=512)

    predictions = model.predict(X_test)
    fitted_predictions = []

    # Only classify as spam if we are 90% sure
    for prediction in predictions:
        if prediction[0] > 0.9:
            fitted_predictions.append([1, 0])
        else:
            fitted_predictions.append([0, 1])

    fitted_predictions = np.array(fitted_predictions)


    accuracy = accuracy_score(y_test, fitted_predictions)
    print(accuracy)

    matrix = confusion_matrix(y_test.argmax(axis=1), fitted_predictions.argmax(axis=1))
    binary = np.array(matrix)

    fig, ax = plot_confusion_matrix(conf_mat=binary)
    plt.show()


def get_neural_network(num_features):
    model = Sequential()

    # Input Layer
    model.add(Dense(50, 
                    activation='relu',
                    input_shape=(num_features, )))

    # Hidden Layer
    model.add(Dense(50, 
                    activation='relu'))

    # Output Layer
    model.add(Dense(2, kernel_initializer='he_normal'))
    model.add(Activation('softmax'))

    model.compile(optimizer='sgd',
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

    return model

if __name__ == '__main__':
    main()
