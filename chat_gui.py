# Creating GUI with tkinter
"""
Module document
"""


def send_chatbot_response(question: str, get_chatbot_response):
    """
        Docstring
    """
    response = get_chatbot_response(question)
    print("Chatbot Response: ", response)


def send_starter_message():
    """
    Docstring
    """
    print("Welcome! Here you can ask whatever questions you want about finance (type quit to exit)")
    print("Ask any question you want.")


def wait_for_user_input():
    """
        Docstring
    """
    question = input("\nAsk your question: ")
    return question


def initialize_chat(get_chatbot_response):
    """
        Docstring
    """
    send_starter_message()

    while True:
        question = wait_for_user_input()

        if question.lower() == "quit":
            break

        send_chatbot_response(question, get_chatbot_response)
