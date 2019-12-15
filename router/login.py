from flask import Blueprint, url_for, redirect, session
from google.auth.transport import requests
from google.oauth2 import id_token

from DB.DAO import comment
from DB.DAO.user import UserDAO
from login import googleLogin

login_blue = Blueprint('login_blue', __name__)

dao = comment.CommentDAO()
gl = googleLogin.GoogleLogin()


@login_blue.route('/google/login')
def google_login():
    redirect_url = gl.login()
    return redirect_url


@login_blue.route('/googleCallback')
def google_callback():
    credentials = gl.google_callback()

    token = credentials['id_token']
    client_id = credentials['client_id']
    id_info = id_token.verify_oauth2_token(token, requests.Request(), client_id)

    try:
        user_dao = UserDAO()
        user = user_dao.select_user_by_email(id_info['email'])

        session['state'] = True
        session['mode'] = 'off'
        session['info'] = user.to_json()
        session['credentials'] = credentials
        return redirect('/')
    except TypeError as e:
        print(e)
        return redirect('/')


@login_blue.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
