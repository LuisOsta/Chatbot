"""
Imports
"""
import numpy as np
from neural_network import create_chatbot, create_model
from chat_gui import initialize_chat
from processor import process_raw_data, create_training_data


INTENTS_FILE_PATH = "./data/intents.json"


training_data, output_labels, words, labels = create_training_data(
    *process_raw_data(INTENTS_FILE_PATH))


print("Training: ", training_data)
print("Output: ", output_labels)

model = create_model(training_data, output_labels)

initialize_chat(create_chatbot(model, labels, words, INTENTS_FILE_PATH))
