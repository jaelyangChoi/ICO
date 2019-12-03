from flask import Blueprint, jsonify, request
from DB.DAO import comment

from ml.model_by_word import model
from ml import ml_predict

route_blue = Blueprint('route_blue', __name__)

dao = comment.CommentDAO()


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
    predict =ml_predict.ModelCombine()
    comment = request.args.get('comment')
    result = predict.total_predict(comment)

    # result = ml.predict(comment)

    return str(result)
