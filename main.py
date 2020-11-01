"""
Imports
"""
import tflearn
import tensorflow as tf

from chat_gui import initialize_chat
from processor import process_raw_data, create_training_data


INTENTS_FILE_PATH = "./data/intents.json"


def create_network(inputs, output):
    """
        Docstring
    """
    tf.compat.v1.reset_default_graph()
    prep_network = tflearn.input_data(shape=[None, len(inputs[0])])
    prep_network = tflearn.fully_connected(prep_network, 8)
    prep_network = tflearn.fully_connected(prep_network, 8)
    final_network = tflearn.fully_connected(
        prep_network, len(output[0]), activation='softmax')

    return final_network


training_data, output_labels = create_training_data(
    *process_raw_data(INTENTS_FILE_PATH))

print("Training: ", training_data)
print("Output: ", output_labels)


network = create_network(training_data, output_labels)
network = tflearn.regression(network)

model = tflearn.DNN(network)
model.fit(training_data, output_labels, n_epoch=1000,
          batch_size=8, show_metric=True)
model.save('model.tflearn')
