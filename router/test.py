from flask import Blueprint, jsonify, request, url_for, redirect, session
from google.auth.transport import requests
from google.oauth2 import id_token
from DB.DAO import comment
from DB.DAO.user import UserDAO
from block.block_class import Block
from login import googleLogin
from ml import ml_predict

test_blue = Blueprint('test_blue', __name__)

dao = comment.CommentDAO()
gl = googleLogin.GoogleLogin()

@test_blue.route('/filter')
def filter():
    block = Block()
    comment = request.args.get('comment')
    result = block.runBlockComment(comment)

    return str(result)

@test_blue.route('/test/ml')
def ml_comment():
    predict = ml_predict.ModelCombine()
    comment = request.args.get('comment')
    result = predict.total_predict(comment)

    return str(result)