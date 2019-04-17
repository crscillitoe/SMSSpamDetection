###############################################################
# features.py - functions that will quantify various features #
#               for a given data point in the data set        #
###############################################################

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- #
#     Generic functions, returns vary function to function    #
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- #


# Number of times a URL appears in the text
def url_count(text):
    return 0

# Number of times a currency symbol appears in the text
def currency_count(text):
    return 0

# Returns the length of the longest series of consecutive numbers in the given text
def longest_numerical_string(text):
    return 0

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
