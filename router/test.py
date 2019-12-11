import time

import pandas as pd
from flask import Blueprint, request

from DB.DAO import comment
from block.block import Block
from login import googleLogin
from ml import ml_predict
from ml.model_by_word.model import ModelByWord

test_blue = Blueprint('test_blue', __name__)

dao = comment.CommentDAO()
gl = googleLogin.GoogleLogin()


@test_blue.route('/filter')
def filter():
    block = Block()
    comment = request.args.get('comment')
    result = block.runBlockComment(comment)

    return str(result)


@test_blue.route('/test/ml/list')
def test_list():
    dd = ModelByWord()
    df = pd.read_csv("./dataset_pumsa_ml/comments_test.csv")
    comments_list = df['comment'].tolist()
    start_time = time.time()
    for comment in comments_list:
        print(str(dd.predict(comment)[0]))
    print("실행시간:" + str(time.time() - start_time))


@test_blue.route('/test/ml')
def ml_comment():
    predict = ml_predict.ModelCombine()
    comment = request.args.get('comment')
    result = predict.total_predict(comment)
    return str(result)


# @route_blue.route('/test/google/login')
# def google_login():
#     redirect_url = gl.login()
#     return redirect_url
#
#
# @route_blue.route('/googleCallback')
# def googleCallback():
#     credentials = gl.google_callback()
#
#     token = credentials['id_token']
#     client_id = credentials['client_id']
#     id_info = id_token.verify_oauth2_token(token, requests.Request(), client_id)
#
#     user_dao = UserDAO()
#     user = user_dao.select_user_by_email(id_info['email'])
#
#     session['state'] = True
#     session['mode'] = 'off'
#     session['info'] = user.to_json()
#     session['credentials'] = credentials
#     return redirect('/')
#
#
# @route_blue.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('index'))
#
#
# @route_blue.route('/test/filter')
# def filter():
#     block = Block()
#     comment = request.args.get('comment')
#     result = block.runBlockComment(comment)
#     return str(result)
