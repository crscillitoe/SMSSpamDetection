import features
from data_loader import load_data
from preprocessing import preprocess_data
import matplotlib
matplotlib.use('TkAgg') # fixes error on mac: https://stackoverflow.com/questions/2512225/matplotlib-plots-not-showing-up-in-mac-osx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
            y_pyth.append(0)
        else:
            y_pyth.append(1)

    X = np.array(X_pyth)
    y = np.array(y_pyth)
    print(X.shape)
    print(y.shape)

if __name__ == '__main__':
    main()
