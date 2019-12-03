from flask import Flask, render_template, Blueprint, request, redirect,url_for, jsonify

from router.update_comment import update_comment_bp
from router.update_keyword import update_keyword_bp

from router import test
from DB.DAO.personal_keyword import PersonalKeywordDAO
# from block import block
import json
import os

from flask import Flask, render_template, request, redirect, url_for
from router import test
from block import block

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, template_folder="templates")
app.secret_key = 'abcdseijvxi'

app.register_blueprint(update_comment_bp)
app.register_blueprint(update_keyword_bp)
app.register_blueprint(test.route_blue)
# app.register_blueprint(db_connection.db_blue)
# app.register_blueprint(block.block_blue)

comments = [{'userID': 'cjl', 'comment': 'test data'},]
keywords = ['sibal', 'byungsin']
mode = 'ICO Service off'

#키워드 db클래스 생성
personal_keywordDB = PersonalKeywordDAO()

@app.route('/googleCallback')
@app.route('/')
def index():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)

    data = json_data['web']
    return render_template('index1.html', cilent_id=data['client_id'])


#DB로부터 댓글과 키워드 받아옴 ->3차필터링 유무
@app.route('/news')
def news():
    global mode
    keywords = personal_keywordDB.select_keywords('abc')
    keywords_str = ', '.join(keywords)
    print(keywords_str)

    if mode == 'ICO Service on':
        print(mode)
        #필터링 함수 ->1차,2차
        #3차 필터링 함수
    return render_template('news1.html', comments=comments, keywords=keywords_str, mode = mode)

@app.route('/filter_mode', methods=['POST'])
def filter_mode():
    global mode
    mode = request.form['mode']
    return redirect(url_for('news'))

#redirect방식
# @app.route('/commentInput', methods=['POST'])
# def commentInput():
#     new_comment = {"userID": request.form['userID'], "comment": request.form['comment']}
#     comments.append(new_comment)
#     return redirect(url_for('news')) #, code=307 => 원래 전송 된대로 요청 유형을 보존



#form 요소:ImmutableMultiDict([('userID', 'userID'), ('comment', 'zzz\r\n')])


if __name__ == '__main__':
    app.run()
