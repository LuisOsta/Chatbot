"""
Module docs
"""
import json
import random
import os.path
import tflearn
import spacy
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
from nltk import word_tokenize

stemmer = LancasterStemmer()

UNCERTAINTY_CUT_OFF = .4

nlp = spacy.load('en_core_web_sm')


def create_network(inputs, output):
    """
        Docstring
    """
    prep_network = tflearn.input_data(shape=[None, len(inputs[0])])
    prep_network = tflearn.fully_connected(prep_network, 8)
    prep_network = tflearn.fully_connected(prep_network, 8)
    final_network = tflearn.fully_connected(
        prep_network, len(output[0]), activation='softmax')

    return final_network


def create_model(inputs, outputs):
    """
    Docstring
    """
    network = create_network(inputs, outputs)
    network = tflearn.regression(network)
    model = tflearn.DNN(network)

    if os.path.isfile("./model/model.tflearn.index"):
        model.load("./model/model.tflearn")
        print("Successfully loaded model.")
    else:
        model.fit(inputs, outputs, n_epoch=1000,
                  batch_size=8, show_metric=True)
        model.save('./model/model.tflearn')

    return model


def create_bag_of_words(sentence, words):
    """
        Docstring
    """
    bag = [0 for _ in range(len(words))]

    s_words = word_tokenize(sentence)
    stemmed_s_words = [stemmer.stem(word.lower()) for word in s_words]

    for s_word in stemmed_s_words:
        for index, chosen_word in enumerate(words):
            if chosen_word == s_word:
                bag[index] = 1

    return np.array(bag)


def get_answer_from_tag(tag: str, data_file_path):
    """
        Docstring
    """
    with open(data_file_path) as file:
        intents = json.load(file)["intents"]

    for intent in intents:
        if intent['tag'] == tag:
            responses = intent['responses']
            return random.choice(responses)

    return "No answer found, please try another question."


def create_chatbot(chatbot_model, labels, words, data_file_path):
    """
        Docstring
    """
    def get_chatbot_response(question, user_name):
        prediction = chatbot_model.predict(
            [create_bag_of_words(question, words)])
        max_index = np.argmax(prediction)
        if prediction[0][max_index] <= UNCERTAINTY_CUT_OFF:
            return "I don't think I understand, can you try again or ask another question?", \
                user_name

        tag = labels[max_index]
        if tag == "introduction":
            new_name = get_name_from_introduction(question)
            return get_answer_from_tag(tag, data_file_path) + ", " + new_name, new_name
        else:
            return get_answer_from_tag(tag, data_file_path), user_name

    return get_chatbot_response


def get_name_from_introduction(text):
    """
    Docstring
    """
    document = nlp(text)
    for entity in document.ents:
        if entity.label_:
            return entity.text

    return ""
