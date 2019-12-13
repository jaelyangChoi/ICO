import os

from flask import redirect, url_for, request
from google_auth_oauthlib.flow import Flow

from config import get_credentials_path

SCOPES = [
    'openid',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/userinfo.email'
]
API_VERSION = 'v2'


class GoogleLogin:
    def __init__(self):
        self._path = get_credentials_path()

    def login(self):
        path = os.path.join(os.getcwd(), 'credentials.json')
        flow = Flow.from_client_secrets_file(path, scopes=SCOPES)
        flow.redirect_uri = url_for('login_blue.googleCallback', _external=True)

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scope='true'
        )

        return redirect(authorization_url)

    def google_callback(self):
        flow = Flow.from_client_secrets_file(self._path, scopes=SCOPES)
        flow.redirect_uri = url_for('login_blue.googleCallback', _external=True)

        authorization_response = request.url
        flow.fetch_token(authorization_response=authorization_response)

        credentials = flow.credentials
        return self.__credentials_to_dict(credentials)

    @staticmethod
    def __credentials_to_dict(credentials):
        return {
            'token': credentials.token,
            'id_token': credentials.id_token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }
