import json


def get_config():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)

    data = json_data['web']
    return data
