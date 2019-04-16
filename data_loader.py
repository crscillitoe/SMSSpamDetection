###############################################################
# load_data.py - functions for loading the data into memory   #
###############################################################

import csv

def load_data(file_path):
    to_return = []
    with open(file_path, encoding='ISO-8859-1') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            m = {
                'category': row['v1'],
                'text': row['v2']
            }
            to_return.append(m)

        return to_return
