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

    spams = []
    hams = []
    for d in data:
        text = d['text']
        if d['category'] == 'spam':
            entry = {
                'currency_count': features.currency_count(text),
                'url_count': features.url_count(text),
                'word_count': features.word_count(text),
                'longest_numerical_string': features.longest_numerical_string(text),
                'average_word_length': features.average_word_length(text),

            }
            spams.append(d['text'])
        else:
            hams.append(d['text'])


    print(hams)
    print(spams)


if __name__ == '__main__':
    main()
