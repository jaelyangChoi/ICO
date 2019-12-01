import json
import os

CLIENT_SECRETS_FILE = "credentials.json"


def get_config():
    with open(CLIENT_SECRETS_FILE) as json_file:
        json_data = json.load(json_file)

    data = json_data['web']
    return data


def get_credentials_path():
    return os.path.join(os.getcwd(), CLIENT_SECRETS_FILE)
