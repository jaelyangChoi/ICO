from flask import Blueprint, jsonify, request, render_template, url_for, redirect, session
from DB.DAO import comment

from ml.model_by_word import model
from login import googleLogin

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
    comment = request.args.get('comment')
    ml = model.ModelByWord()

    result = ml.predict(comment)

    return str(result)


@route_blue.route('/test/google/login')
def google_login():
    redirect_url = gl.login()
    return redirect_url


@route_blue.route('/googleCallback')
def googleCallback():
    result = gl.google_callback()
    session['id_token'] = result['id_token']
    return redirect('/')


@route_blue.route('/logout')
def logout():
    if 'state' in session:
        del session['state']

    return redirect(url_for('index'))
