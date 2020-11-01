"""
Imports
"""
import json
import os.path
import pickle
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
from nltk import word_tokenize

stemmer = LancasterStemmer()


def process_raw_data(filepath):
    """
    Docstring
    """

    if(os.path.isfile("./data/data.pickle")):
        return [], [], [], []
    else:
        words = []
        labels = []
        docs_x = []
        docs_y = []
        with open(filepath) as file:
            intents = json.load(file)["intents"]

        for intent in intents:
            for pattern in intent["patterns"]:
                word_tokens = word_tokenize(pattern)
                words.extend(word_tokens)

                docs_x.append(word_tokens)
                docs_y.append(intent['tag'])
            if intent['tag'] not in labels:
                labels.append(intent['tag'])

        stemmed_words = sorted(
            list(set([stemmer.stem(w.lower()) for w in words if w not in "?"])))
        sorted_labels = sorted(labels)

        return docs_x, docs_y, stemmed_words, sorted_labels


# initialize_chat()

def create_training_data(docs_x, docs_y, stemmed_words, labels):
    """
    Doc string
    """

    try:
        with open("./data/data.pickle", "rb") as file:
            training, output = pickle.load(file)
            return training, output
    except:
        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]

        for index, doc in enumerate(docs_x):
            bag = []

            stemmed_pattern = [stemmer.stem(w) for w in doc]

            for stemmed_word in stemmed_words:
                if stemmed_word in stemmed_pattern:
                    bag.append(1)
                else:
                    bag.append(0)
            output_row = out_empty[:]
            output_row[labels.index(docs_y[index])] = 1

            training.append(bag)
            output.append(output_row)

        training = np.array(training)
        output = np.array(output)

        with open("./data/data.pickle", "wb") as file:
            pickle.dump((training, output), file)
        return training, output
