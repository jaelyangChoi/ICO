from flask import Flask, render_template, request, redirect, url_for, session
from router.update_comment import update_comment_bp
from router.update_keyword import update_keyword_bp
from DB.DAO.comment import CommentDAO
from DB.DAO.personal_keyword import PersonalKeywordDAO
from block.filtering import filtering
import json
import os
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

# 임시 댓글, 키워드
# comments = [{'userID': session['id'], 'comment': 'test data'},]
# keywords = ['sibal', 'byungsin']

# 댓글, 키워드 db클래스 생성
CommentDAO = CommentDAO()
personal_keywordDB = PersonalKeywordDAO()


@app.route('/googleCallback')
@app.route('/')
def index():
    with open('credentials.json') as json_file:
        json_data = json.load(json_file)
    data = json_data['web']
    return render_template('index.html', cilent_id=data['client_id'])


# DB로부터 댓글과 키워드 받아와 필터링해 반환
@app.route('/news')
def news():
    mode =True
    keywords = personal_keywordDB.select_keywords('cjl0701')
    keywords_str = ', '.join(keywords)
    print(keywords_str)

    # 전체 댓글 리로드
    comments = CommentDAO.select_comments_by_url('http://localhost:5000/news')
    # for comment in comments:
    #   print(comment.get_comment()) 반환 값 {'idx': 1, 'text': '왜구들이 미쳐 날뛰네', 'propriety': 0, 'ML_learning': 0, 'url': '', 'writer': '1', 'time': datetime.datetime(2019, 12, 2, 19, 5, 19)}

    # 필터링 서비스
    if mode:
        comments = filtering(comments)

    return render_template('news1.html', comments=comments, keywords=keywords_str, mode='on')


@app.route('/filter_mode', methods=['POST'])
def filter_mode():
    session['mode'] = request.form['mode']
    return redirect(url_for('news'))


if __name__ == '__main__':
    app.run()

# redirect방식
# @app.route('/commentInput', methods=['POST'])
# def commentInput():
#     new_comment = {"userID": request.form['userID'], "comment": request.form['comment']}
#     comments.append(new_comment)
#     return redirect(url_for('news')) #, code=307 => 원래 전송 된대로 요청 유형을 보존


# form 요소:ImmutableMultiDict([('userID', 'userID'), ('comment', 'zzz\r\n')])