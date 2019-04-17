import features
from data_loader import load_data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    file_path = 'spam.csv'
    data = load_data(file_path)

    spams = []
    hams = []
    for d in data:
        if d['category'] == 'spam':
            spams.append(d['text'])
        else:
            hams.append(d['text'])

    plot_function_to_test('Number of "Free" Occurences', hams, spams)


def plot_function_to_test(plot_title, hams, spams):
    spam_total = 0
    for spam in spams:
        spam_total += features.longest_numerical_string(spam)

    ham_total = 0
    for ham in hams:
        ham_total += features.longest_numerical_string(ham)

    classes = ['Spam', 'Ham']

    percent_spam = (spam_total / len(spams)) 
    percent_ham  = (ham_total / len(hams)) 

    percentages = pd.DataFrame({
        'free':(percent_spam, percent_ham)
    }, index=classes)

    graph = percentages.free.plot(kind='bar', title='Average length of longest numerical string')
    plt.show()



if __name__ == '__main__':
    main()
