"""
Imports
"""
import json
from flask import Flask, send_from_directory, request
import os
import logging
import subprocess

from werkzeug.exceptions import BadRequest
from neural_network import create_chatbot, create_model
from chat_gui import initialize_chat
from processor import process_raw_data, create_training_data

app = Flask(__name__, static_folder="client/build/")
logging.getLogger('tflearn').setLevel(logging.CRITICAL)
logging.getLogger('tensorflow').setLevel(logging.CRITICAL)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
INTENTS_FILE_PATH = "./data/intents.json"


# subprocess.call('clear')
training_data, output_labels, words, labels = create_training_data(
    *process_raw_data(INTENTS_FILE_PATH))

model = create_model(training_data, output_labels)

get_chatbot_response = create_chatbot(
    model, labels, words, INTENTS_FILE_PATH)


@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    """
        Docstring
    """
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route("/chatbot/response", methods=["POST"])
def send_chatbot_response():
    """
        Docstring
    """
    try:
        text = request.get_json()['data']['text']
        return get_chatbot_response(text)
    except BadRequest as error:
        print(error)
        return "Error"


if __name__ == "__main__":
    subprocess.call('clear')
    app.run(use_reloader=True, port=5000, threaded=True)
