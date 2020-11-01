"""
Imports
"""
import os
import logging
from flask import Flask, send_from_directory, request

from werkzeug.exceptions import BadRequest
from neural_network import create_chatbot, create_model
from processor import process_raw_data, create_training_data

application = Flask(__name__, static_folder="client/build/")
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


@application.route("/", defaults={'path': ''})
@application.route('/<path:path>')
def serve_react(path):
    """
        Docstring
    """
    if path != "" and os.path.exists(application.static_folder + '/' + path):
        return send_from_directory(application.static_folder, path)
    else:
        return send_from_directory(application.static_folder, 'index.html')


@application.route("/chatbot/response", methods=["POST"])
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
    port = int(os.environ.get("PORT", 5000))
    application.run(port=port, threaded=True, debug=True)
