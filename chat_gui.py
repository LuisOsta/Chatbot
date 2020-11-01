# Creating GUI with tkinter
"""
Module document
"""


def chatbot_response(msg: str):
    """
    Docstring
    """
    return msg


def send_chatbot_response(question: str):
    """
        Docstring
    """
    response = chatbot_response(question)
    print("Chatbot Response: ", response)


def send_starter_message():
    """
    Docstring
    """
    print("Welcome! Here you can ask whatever questions you want about finance")
    print("Ask any question you want.")


def wait_for_user_input():
    """
        Docstring
    """
    question = input("\nAsk your question: ")
    return question


def initialize_chat():
    """
        Docstring
    """
    send_starter_message()

    while True:
        question = wait_for_user_input()
        send_chatbot_response(question)
