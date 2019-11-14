from flask import Blueprint, jsonify
from DB import DAO

route_blue = Blueprint('route_blue', __name__)

dao = DAO.DatabaseDAO()


@route_blue.route('/test/comments/<url>')
def select_comments(url):
    result = dao.selectCommentsByURL(url)

    temp = []
    for data in result:
        print(data.to_json())
        temp.append(data.to_json())

    return jsonify(temp)
