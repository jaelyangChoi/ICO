from flask import Blueprint, jsonify, request
from DB.DAO import comment

from ml.model_by_word import model

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
    comment = request.args.get('comment')
    ml = model.ModelByWord()

    result = ml.predict(comment)

    return str(result)
