from flask import Flask, render_template, Blueprint, request, redirect,url_for, jsonify

from router.update_comment import update_comment_bp
from router.update_keyword import update_keyword_bp
from router import test
from DB.DAO.personal_keyword import PersonalKeywordDAO
# from block import block

app = Flask(__name__, template_folder="templates")

app.register_blueprint(update_comment_bp)
app.register_blueprint(update_keyword_bp)
app.register_blueprint(test.route_blue)
# app.register_blueprint(db_connection.db_blue)
# app.register_blueprint(block.block_blue)

comments = [{'userID': 'cjl', 'comment': 'test data'},]
keywords = ['sibal', 'byungsin']
mode = '개인 필터 on'

#db클래스 생성
personal_keywordDB = PersonalKeywordDAO()

@app.route('/googleCallback')
@app.route('/')
def index():
   return render_template('index.html')

#DB로부터 댓글과 키워드를 전달 받아야함
@app.route('/news', methods=["POST"])
def news():
    global mode
    #DB로부터 댓글과 키워드 받아옴
    #personal_keywordDB.insert_keyword('abc','shit')
    #keywords = personal_keywordDB.select_keywords('abc')
    #print(keywords)
    keywords_str = ', '.join(keywords)
    if mode == '개인 필터 on':
        print(mode)
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
