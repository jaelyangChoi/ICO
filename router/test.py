from flask import Blueprint, jsonify, request, url_for, redirect, session
from google.auth.transport import requests
from google.oauth2 import id_token

from DB.DAO import comment
from DB.DAO.user import UserDAO
from block.block_class import Block
from login import googleLogin
from ml import ml_predict

route_blue = Blueprint('route_blue', __name__)

dao = comment.CommentDAO()
gl = googleLogin.GoogleLogin()


@route_blue.route('/test/comments/<url>')
def select_comments(url):
    result = dao.select_comments_by_url(url)

    temp = []
    for data in result:
        print(data.to_json())
        temp.append(data.to_json())

    return jsonify(temp)


@route_blue.route('/test/ml')
def ml_comment():
    predict = ml_predict.ModelCombine()
    comment = request.args.get('comment')
    result = predict.total_predict(comment)

    return str(result)


@route_blue.route('/test/google/login')
def google_login():
    redirect_url = gl.login()
    return redirect_url


@route_blue.route('/googleCallback')
def googleCallback():
    credentials = gl.google_callback()

    token = credentials['id_token']
    client_id = credentials['client_id']
    id_info = id_token.verify_oauth2_token(token, requests.Request(), client_id)

    user_dao = UserDAO()
    user = user_dao.select_by_email(id_info['email'])

    session['state'] = True
    session['mode'] = 'off'
    session['info'] = user.get_user()
    session['credentials'] = credentials
    return redirect('/')


@route_blue.route('/logout')
def logout():
    session.clear()

    return redirect(url_for('index'))


@route_blue.route('/test/filter')
def filter():
    block = Block()
    comment = request.args.get('comment')
    result = block.runBlockComment(comment)

    return str(result)
