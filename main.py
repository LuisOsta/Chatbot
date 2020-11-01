"""
Imports
"""
import os
import logging
import subprocess
from neural_network import create_chatbot, create_model
from chat_gui import initialize_chat
from processor import process_raw_data, create_training_data


logging.getLogger('tflearn').setLevel(logging.CRITICAL)
logging.getLogger('tensorflow').setLevel(logging.CRITICAL)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
INTENTS_FILE_PATH = "./data/intents.json"


subprocess.call('clear')

training_data, output_labels, words, labels = create_training_data(
    *process_raw_data(INTENTS_FILE_PATH))

model = create_model(training_data, output_labels)

initialize_chat(create_chatbot(model, labels, words, INTENTS_FILE_PATH))
