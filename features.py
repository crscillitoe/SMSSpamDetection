###############################################################
# features.py - functions that will quantify various features #
#               for a given data point in the data set        #
###############################################################

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- #
#     Generic functions, returns vary function to function    #
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- #


import re

# Number of times a URL appears in the text
def url_count(text):
    # https://www.geeksforgeeks.org/python-check-url-string/
    url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url, text.lower())
    return len(urls)

# Number of times a currency symbol appears in the text
def currency_count(text):
    count = 0
    symbols = ['$', '£']
    for word in text.split():
      for symbol in symbols:
        if symbol in word:
          count += 1
    return count

# Returns the length of the longest series of consecutive numbers in the given text
def longest_numerical_string(text):
    numbers = '\d+'
    sequences = re.findall(numbers, text)
    longest = 0
    for sequence in sequences:
      if len(sequence) > longest:
        longest = len(sequence)
    return longest

# Returns the average word length in the given text
def average_word_length(text):
    words = text.split(' ')
    length = 0
    for word in words:
        length += len(word)
    return length/len(words)

# Number of times the word 'win' occurs in the given text
def num_win_occurences(text):
    words = text.split(' ')
    count = 0
    for word in words:
        word = word.lower()
        if word == 'win' or word == 'winning':
            count += 1
    return count

# Number of times the word 'free' occurs in the given text
def num_free_occurences(text):
    words = text.split(' ')
    count = 0
    for word in words:
        word = word.lower()
        if word == 'free':
            count += 1
    return count
