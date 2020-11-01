"""
    Module
"""
users = dict()


def get_user_preferences(user_name):
    """
    Docstring
    """
    old_user = users.get(user_name, {"name": user_name, "preferences": []})
    return old_user['preferences']


def update_user_preference(user_name: str, label: int):
    """
    Docstring
    """

    if len(user_name) == 0:
        return

    if user_name in users:
        old_user = users.get(user_name)
        new_preferences = list(set([label] + old_user['preferences']))

        new_user = {"name": user_name, "preferences": new_preferences}
        users[user_name] = new_user

    else:
        new_user = {"name": user_name, "preferences": [label]}
        users[user_name] = new_user


def get_weighted_predictions(predictions, user_name):
    """
    Docstring
    """
    preferences = get_user_preferences(user_name)

    if len(preferences) == 0:
        return predictions

    for index, _ in enumerate(predictions):
        if index in preferences:
            predictions[index] += .1
        else:
            predictions[index] -= .1

    return predictions
