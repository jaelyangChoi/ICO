from flask import Flask, Blueprint, render_template, request, jsonify

update_bp = Blueprint('update', __name__)

comments = [{'userID': 'cjl', 'comment': 'test data'}]
keywords = ['sibal', 'byungsin']


@update_bp.route('/updateComment', methods=['POST'])
def updateComment():
    new_comment = {"userID": request.form['userID'], "comment": request.form['comment']}
    comments.insert(0, new_comment)
    return jsonify(comments)


@update_bp.route('/updateKeyword', methods=['POST'])
def updateKeyword():
    keywords.append(request.form['keyword'])
    keywordStr = ', '.join(keywords)
    print(keywordStr)
    return jsonify(keywordStr)

# @view_blueprint.route('/googleCallback')
# @view_blueprint.route('/')
# def index():
#     print(view_blueprint.root_path)
#     return render_template('index.html')
#
#
# @view_blueprint.route('/news')
# def news():
#     #posts = Post.query.all()
#     return render_template('news1.html')
#     #return "hello"
