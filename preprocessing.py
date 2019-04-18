################################################################
# preprocessing.py - functions for processing data once loaded #
################################################################

def preprocess_data(data):
  replace_escaped_characters(data)

def replace_escaped_characters(data):
  for message in data:
    # print(message['text'])
    message['text'] = message['text'].replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&apos;', '\'')
